import subprocess

def test_output():
    result = subprocess.run(['python3', 'app.py'], stdout=subprocess.PIPE)
    assert b"Hello from CI/CD" in result.stdout
