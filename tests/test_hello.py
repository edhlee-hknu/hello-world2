# tests/test_hello.py
import subprocess, sys, pathlib

def test_prints_hello_world():
    """
    The student's main.py should print exactly:
        Hello, World!
    including the capital letters and exclamation mark,
    followed by a newline (which we strip before comparing).
    """
    # Path to the repo root so the test works no matter where it's run
    repo_root = pathlib.Path(__file__).resolve().parents[1]
    
    # Run main.py as a separate process
    result = subprocess.run(
        [sys.executable, repo_root / "main.py"],
        capture_output=True, text=True
    )
    
    # 1️⃣ assert the script exited normally
    assert result.returncode == 0, "main.py terminated with an error"

    # 2️⃣ assert the output is exactly "Hello, World!"
    assert result.stdout.strip() == "Hello, World!", (
        f'Expected "Hello, World!" but got {result.stdout!r}'
    )
