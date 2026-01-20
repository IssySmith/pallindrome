from main import is_palindrome

def test_is_palindrome_true():
    assert is_palindrome(121) == True
    assert is_palindrome(12121) == True
    assert is_palindrome("hannah") == True
    assert is_palindrome("Hannah") == True
    assert is_palindrome("race car") == True
    
    
def test_is_palindrome_false():
    assert is_palindrome(122) == False
    assert is_palindrome(12122) == False
    assert is_palindrome("steve") == False
    assert is_palindrome("Steve") == False
    assert is_palindrome("race cart") == False