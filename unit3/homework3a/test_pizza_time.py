from byu_pytest_utils import max_score, test_files, dialog


@max_score(5)
@dialog(
    test_files / "pizza-time.dialog.txt",
    "pizza_time.py",
)
def test_pizza_time(): ...
