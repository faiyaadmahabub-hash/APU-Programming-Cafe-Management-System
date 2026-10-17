# Verification

Date: 17 October 2026. Environment: Windows, PowerShell, Python 3.10.9; standard library application and checks. Pillow 12.0.0 was used only to render the transcript image; it is not an application dependency.

| Command | Result / scope |
|---|---|
| `python -B -m unittest discover -s tests -v` | 6 tests passed. Python 3.10 parsing; all four role login/dashboard/exit paths; repaired module/trainer persistence and legacy request operations. |
| `python -B scripts/demo.py` | Exit 0. Real administrator dashboard login/exit and module API create/schedule/add-student/pay/delete in a disposable app copy. Assertions confirm persisted invoice and deletion. |
| `git diff -- database` | No bundled record changes. |

The demo replies shown in the transcript are the prompt-fed inputs from `scripts/demo.py`, all fictional. Capture command (PowerShell):

```powershell
python -B scripts/demo.py | Set-Content -Encoding utf8 docs/assets/demo-transcript.txt
```

`docs/assets/demo-transcript.png` renders that captured text with Pillow and Consolas on a dark background. It is a transcript rendering, not a screenshot of a terminal or desktop app. No native browser/desktop screenshot was available for this console application.

Passing checks cover the listed operations. They do not establish correctness of every menu, transactional enrolment, consistent duplicate invoices, authentication security or concurrent writes. The remaining known issues are retained in `PROJECT_GUIDE.md`. The report PDF stays ignored and local.
