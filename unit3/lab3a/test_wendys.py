from byu_pytest_utils import dialog, max_score, test_files


@dialog(test_files / 'wendys.txt',
        'wendys.py')
@max_score(5)
def test_wendys(): ...
