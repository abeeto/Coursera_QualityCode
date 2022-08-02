#lists and tuples
from operator import is_


def is_palindrome(s):
    """ (str) -> bool
    Return True if and only if s is a palindrome
    is_palindrome('noon'): true
    is_palindrome('racecar'): true
    is_palindrome('dented'): false
    """
# algorithm one: reverse and compare string
    # s_rev = ""
    # for i in range(len(s)-1, -1, -1):
    #     s_rev += s[i]
    # return s_rev == s
# algorithm two: split in "half", reverse and compare second half with first half
    # sHalfOne = s[0:len(s)//2]
    # if (len(s) % 2 == 0):
    #     sHalfTwo = s[len(s)//2:len(s)]
    # else:
    #     sHalfTwo = s[len(s)//2+1:len(s)]
    # sHalfTwo_rev = ""
    # for i in range(len(sHalfTwo)-1, -1, -1):
    #     sHalfTwo_rev += sHalfTwo[i]
    # return sHalfTwo_rev == sHalfOne
# algorithm three: take it in pairs and compare
    # i_rev = len(s)-1
    # for i in range(0, len(s)//2):
    #     if s[i] != s[i_rev]:
    #         return False
    #     else:
    #         i_rev -= 1
    # return True
