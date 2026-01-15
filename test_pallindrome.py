from main import is_pallindrome

def test_is_pallindrome_true():
    assert is_pallindrome(121) == True
    assert is_pallindrome(12121) == True
    assert is_pallindrome(323) == True
    assert is_pallindrome(111) == True
    assert is_pallindrome("hannah") == True
    
def test_is_pallindrome_false():
    assert is_pallindrome(112) == False
    assert is_pallindrome(112345) == False
    assert is_pallindrome(322) == False
    assert is_pallindrome("minimum") == False