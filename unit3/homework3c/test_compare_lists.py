from byu_pytest_utils import max_score, dialog, test_files


@max_score(2)
@dialog(
    test_files / "compare_lists_fruit.dialog.txt",
    "compare_lists.py"
)
def test_compare_lists_fruit(): ...

@max_score(2)
@dialog(
    test_files / "compare_lists_vegetables.dialog.txt",
    "compare_lists.py"
)
def test_compare_lists_vegetables(): ...

@max_score(2)
@dialog(
    test_files / "compare_lists_equal.dialog.txt",
    "compare_lists.py"
)
def test_compare_lists_equal(): ...