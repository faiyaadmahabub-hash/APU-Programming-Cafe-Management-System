"""Run real dashboard/API code against temporary fictional records only."""
import asyncio
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]

async def dashboard(app):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    env['PATH'] = str(Path(sys.executable).parent) + os.pathsep + env.get('PATH', '')
    process = await asyncio.create_subprocess_exec(
        sys.executable, '-B', 'main.py', cwd=app, env=env,
        stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    async def interact():
        for prompt, reply in [('Enter choice:', '1'), ('Enter choice:', '1'),
                              ('Name:', 'Demo administrator'), ('Password:', 'demo-only'),
                              ('Enter choice:', '4')]:
            chunk = await process.stdout.readuntil(prompt.encode())
            print(chunk.decode(), end='')
            print(' ' + reply)
            process.stdin.write((reply + '\n').encode())
            await process.stdin.drain()
        output, errors = await process.communicate()
        print(output.decode(), end='')
        if process.returncode or errors:
            raise RuntimeError(errors.decode())
    try:
        await asyncio.wait_for(interact(), timeout=15)
    finally:
        if process.returncode is None:
            process.kill()
            await process.wait()

with tempfile.TemporaryDirectory() as folder:
    app = Path(folder)
    for source in ROOT.glob('*.py'):
        shutil.copy2(source, app / source.name)
    for name in ('api', 'display'):
        shutil.copytree(ROOT / name, app / name, ignore=shutil.ignore_patterns('__pycache__'))
    (app / 'database').mkdir()
    for role in ('administrator', 'lecturer', 'trainer', 'student'):
        rows = [{'id': 'demo-admin', 'name': 'Demo administrator', 'password': 'demo-only'}] if role == 'administrator' else []
        (app / 'database' / (role + 's.json')).write_text(json.dumps(rows))
    for name in ('modules', 'feedbacks'):
        (app / 'database' / (name + '.json')).write_text('{}')
    print('APU Programming Cafe | fictional temporary data | 2026-10-17')
    print('Dashboard run: python -B main.py (prompt-fed replies shown below)\n')
    asyncio.run(dashboard(app))
    print('\nAPI persistence demonstration:')
    result = subprocess.run([sys.executable, '-B', '-c', '''
import json
from pathlib import Path
from api import module
key = module.create('demo-trainer', 'python', 'beginner', 'Python demo')
module.add_schedule(key, '2026-11-02T10:00:00')
module.add_student(key, 'demo-student', 'november')
module.pay_student_invoice(key, 'demo-student')
saved = json.loads(Path('database/modules.json').read_text())[key]
assert saved['students'][0]['invoice'] == 0
print('Module: ' + saved['name'])
print('Schedule: ' + saved['schedule'][0])
print('Student invoice after module API payment: ' + str(saved['students'][0]['invoice']))
module.delete(key)
assert json.loads(Path('database/modules.json').read_text()) == {}
print('Module deletion persisted: yes')
'''], cwd=app, capture_output=True, text=True, timeout=15, check=True)
    print(result.stdout, end='')
    print('Temporary records removed on exit; bundled database unchanged.')
