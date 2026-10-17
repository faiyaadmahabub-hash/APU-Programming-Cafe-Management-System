"""Regression checks use temporary app copies and fictional JSON fixtures."""
import ast
import asyncio
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RepairedWorkflows(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.app = Path(self.temp.name)
        for source in ROOT.glob('*.py'):
            shutil.copy2(source, self.app / source.name)
        for folder in ('api', 'display'):
            shutil.copytree(ROOT / folder, self.app / folder, ignore=shutil.ignore_patterns('__pycache__'))
        (self.app / 'database').mkdir()
        accounts = {}
        for role in ('administrator', 'lecturer', 'trainer', 'student'):
            accounts[role] = {'id': role + '-1', 'name': role, 'password': 'example-password'}
        accounts['lecturer']['requests'] = {}
        accounts['trainer'].update(modules=[], feedbacks=[])
        accounts['student'].update(
            lecturer='lecturer-1', tp_number='DEMO001', email='student@example.invalid',
            contact_number='0000000000', address='Example campus', modules=[], requests={})
        for role, account in accounts.items():
            (self.app / 'database' / (role + 's.json')).write_text(json.dumps([account]), encoding='utf-8')
        for filename in ('modules.json', 'feedbacks.json'):
            (self.app / 'database' / filename).write_text('{}', encoding='utf-8')

    def run_code(self, source):
        result = subprocess.run(
            [sys.executable, '-B', '-c', textwrap.dedent(source)], cwd=self.app,
            capture_output=True, text=True, timeout=15)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def read_database(self, name):
        return json.loads((self.app / 'database' / (name + '.json')).read_text(encoding='utf-8'))

    def test_all_source_files_parse_on_python_310(self):
        for source in self.app.rglob('*.py'):
            with self.subTest(file=str(source.relative_to(self.app))):
                try:
                    ast.parse(source.read_text(encoding='utf-8'), filename=str(source), feature_version=(3, 10))
                except SyntaxError as error:
                    self.fail(str(error))

    def test_each_role_can_log_in_open_dashboard_and_exit(self):
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
        env['PATH'] = str(Path(sys.executable).parent) + os.pathsep + env.get('PATH', '')
        for number, role, exit_choice in ((1, 'administrator', 4), (2, 'lecturer', 4), (3, 'trainer', 5), (4, 'student', 5)):
            with self.subTest(role=role):
                # Feed the child dashboard only after the login process launches it;
                # preloading a pipe lets the parent's input buffer swallow its input.
                async def login_and_exit():
                    process = await asyncio.create_subprocess_exec(
                        sys.executable, '-B', 'main.py', cwd=self.app, env=env,
                        stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE,
                        stderr=asyncio.subprocess.PIPE)

                    async def interact():
                        output = b''
                        for prompt, reply in (('Enter choice:', str(number)), ('Enter choice:', '1'), ('Name:', role), ('Password:', 'example-password'), ('Enter choice:', str(exit_choice))):
                            output += await process.stdout.readuntil(prompt.encode())
                            process.stdin.write((reply + '\n').encode())
                            await process.stdin.drain()
                        tail, errors = await process.communicate()
                        return process.returncode, (output + tail).decode(), errors.decode()

                    try:
                        return await asyncio.wait_for(interact(), timeout=15)
                    finally:
                        if process.returncode is None:
                            process.stdin.close()
                            process.kill()
                            await process.wait()

                returncode, output, errors = asyncio.run(login_and_exit())
                self.assertEqual(returncode, 0, errors)
                self.assertNotIn('Traceback', errors)
                self.assertIn(role + ' dashboard', output.lower())

    def test_module_schedule_enrollment_payment_and_deletion_persist(self):
        self.run_code('''
            import json
            from pathlib import Path
            from api import module
            key = module.create('trainer-1', 'python', 'beginner', 'Python demo')
            module.add_student(key, 'student-1', 'january')
            module.add_student(key, 'student-2', 'february')
            module.add_schedule(key, '2026-02-02T10:00:00')
            module.add_schedule(key, '2026-02-01T10:00:00')
            module.edit_schedule(key, 1, '2026-01-31T10:00:00')
            module.remove_schedule(key, 1)
            module.pay_student_invoice(key, 'student-1')
            saved = json.loads(Path('database/modules.json').read_text())
            assert saved[key]['schedule'] == ['2026-01-31T10:00:00'], saved
            assert [row['invoice'] for row in saved[key]['students']] == [0, 1000], saved
            module.remove_student('student-1')
            saved = json.loads(Path('database/modules.json').read_text())
            assert saved[key]['students'] == [{'id': 'student-2', 'enrolment_month': 'february', 'invoice': 1000}], saved
            module.delete(key)
        ''')
        self.assertEqual(self.read_database('modules'), {})

    def test_trainer_profile_module_and_feedback_changes_persist(self):
        self.run_code('''
            from api import trainer
            trainer.add_module('trainer-1', 'module-demo')
            trainer.add_feedback('trainer-1', 'feedback-demo')
            trainer.change_name('trainer-1', 'Updated demo trainer')
            trainer.change_password('trainer-1', 'updated-example-password')
        ''')
        self.assertEqual(self.read_database('trainers'), [{
            'id': 'trainer-1', 'name': 'Updated demo trainer',
            'password': 'updated-example-password', 'modules': ['module-demo'],
            'feedbacks': ['feedback-demo']}])

    def test_deleting_trainer_removes_assigned_modules(self):
        self.run_code('''
            from api import module, trainer
            key = module.create('trainer-1', 'python', 'beginner', 'Python demo')
            trainer.add_module('trainer-1', key)
            assert trainer.delete('trainer-1') is True
        ''')
        self.assertEqual(self.read_database('trainers'), [])
        self.assertEqual(self.read_database('modules'), {})

    def test_legacy_student_request_can_be_displayed_and_deleted(self):
        result = self.run_code('''
            import student
            key = student.request('student-1', 'python', 'beginner')
            student.show_request_status('student-1')
            student.delete_requests('student-1', key)
        ''')
        self.assertIn('Module: python', result.stdout)
        self.assertIn('Status: pending', result.stdout)
        self.assertEqual(self.read_database('students')[0]['requests'], {})


if __name__ == '__main__':
    unittest.main()
