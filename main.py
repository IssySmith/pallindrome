def is_palindrome(input):
    s = str(input)
    if s == s[::-1]:
        return True
    else:
        return False