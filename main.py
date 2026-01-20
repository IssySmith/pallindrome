def is_palindrome(input_v):
    s = str(input_v).lower()
    if s == s[::-1]:
        return True
    else:
        return False