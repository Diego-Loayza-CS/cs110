from byu_pytest_utils import max_score, test_files, dialog


@max_score(10)
@dialog(
    test_files / "simplify.dialog.txt",
    "simplify.py"
)
def test_simplify(): ...