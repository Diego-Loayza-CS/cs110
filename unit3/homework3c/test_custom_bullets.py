from byu_pytest_utils import max_score, dialog, test_files


@max_score(7)
@dialog(
    test_files / "custom_bullets.dialog.txt",
    "custom_bullets.py"
)
def test_custom_bullets(): ...

@max_score(7)
@dialog(
    test_files / "custom_bullets.dialog.txt",
    "custom_bullets.py"
)
def test_custom_bullets2(): ...

