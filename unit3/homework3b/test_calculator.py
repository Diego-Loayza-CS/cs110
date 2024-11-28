from byu_pytest_utils import dialog, max_score, test_files


@max_score(10)
@dialog(
    test_files / "calculator.dialog.txt",
    "calculator.py"
)
def test_calculator(): ...
