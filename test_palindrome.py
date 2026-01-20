from main import is_palindrome

def test_palindrome_true():
    assert is_palindrome(121) == True
    
def test_palindrome_false():
    assert is_palindrome(122) == False