from slapping.slap import slap
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ("Bob", "Slapped Bob"),
    ("Alice", "Slapped Alice"),
    ("Carol", "Slapped Carol"),
    ("Dave", "Slapped Dave"),
    ("Eve", "Slapped Eve"),
    ("Frank", "Slapped Frank"),
])
def test_slap(test_input, expected):
    assert slap(test_input) == expected


# def test_db_slap(db_conn):
#     db_conn.read_slaps()
#     assert ...

def test_print(capture_stdout):
    print("hello")
    assert capture_stdout["stdout"] == "hello\n"
