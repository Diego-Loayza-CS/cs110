from byu_pytest_utils import max_score, dialog, test_files


@max_score(7)
@dialog(
    test_files / "words.dialog.txt",
    "words.py"
)
def test_words(): ...