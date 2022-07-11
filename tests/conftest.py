import pytest
import sys


# all our session conext is stored in the session object
@pytest.fixture(scope="session")
def db_connection():
    db = None
    url = None
    print("Connecting to database...")

    with db.connect(url) as conn:
        yield conn


@pytest.fixture
def capture_stdout(monkeypatch):
    buffer = {"stdout": "", "write_calls": 0}

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.stdout, 'write', fake_write)
    return buffer
