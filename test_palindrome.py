from main import test_palindrome

def test_palindrome_true():
    assert test_palindrome(121) == True
    
def test_palindrome_false():
    assert test_palindrome(122) == False