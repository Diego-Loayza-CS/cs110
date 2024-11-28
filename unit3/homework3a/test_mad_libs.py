from byu_pytest_utils import dialog, max_score, test_files


@max_score(5)
@dialog(
    test_files / 'mad-libs-short.dialog.txt',
    'mad_libs_short.py'
)
def test_mad_libs_short(): ...


@max_score(5)
@dialog(
    test_files / 'mad-libs.dialog.txt',
    'mad_libs.py',
)
def test_mad_libs(): ...

