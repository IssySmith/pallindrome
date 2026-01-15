# This function ensure that the input is a string
# then using string handling it reverses the order of the string
# which then compare it to the original string 

def is_pallindrome(input_value):
    s = str(input_value)
    if s == s[::-1]:
        return True
    else:
        return False