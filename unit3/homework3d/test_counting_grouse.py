from byu_pytest_utils import max_score, dialog, test_files


@max_score(10)
@dialog(
    test_files / "counting_grouse.dialog.txt",
    "counting_grouse.py"
)
def test_counting_grouse(): ...