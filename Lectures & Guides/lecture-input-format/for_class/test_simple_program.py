from byu_pytest_utils import max_score, dialog, test_files

@max_score(5)
@dialog(
    test_files / 'simple.dialog.txt', 'simple_program.py'
)
def test_program(): ...

    
@max_score(5)
@dialog(
    test_files / 'simple2.dialog.txt', 'simple_program.py'
)
def test_program2(): ...
  
