def is_palindrome(s):
    """ (str) -> bool
    Return True if and only if s is a palindrome
    is_palindrome('noon'): true
    is_palindrome('racecar'): true
    is_palindrome('dented'): false
    """
    return s == reverse(s)


def reverse(s):
    '''(str) -> str
    returns a reversed version of s

    reverse('hello')
    'olleh'
    '''
    rev = ""
    # for each character in s, add that char to the beginning of rev.
    for ch in s:
        rev = ch + rev
    return rev


print(is_palindrome("racecar"))
