from main import is_palindrome

def test_is_palindrome_true():
    assert is_palindrome(121) == True
    assert is_palindrome(12121) == True
    
def test_is_palindrome_false():
    assert is_palindrome(122) == False
    assert is_palindrome(12122) == False