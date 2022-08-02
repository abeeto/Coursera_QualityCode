def is_palindrome(s):
    """ (str) -> bool
    Return True if and only if s is a palindrome
    is_palindrome('noon'): true
    is_palindrome('racecar'): true
    is_palindrome('dented'): false
    """
    stop_i = len(s) // 2
    start_i = len(s) - stop_i
    halfOne = s[0:stop_i]
    halfTwo = s[start_i:]
    return halfOne == reverse(halfTwo)


def reverse(s):
    rev = ''
    for ch in s:
        rev = ch + rev
    return rev


print(is_palindrome("racecar"))
