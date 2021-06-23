def helper(s, l, r):
    if s[l] != s[r]:
        return False
    if l < r:
        return helper(s, l + 1, r - 1)
    return True

def isPalindrome(s):
    ''' Check that string is palindrome, uses helper function to recursively check'''
    if not s:
        return True
    return helper(s, 0, len(s) - 1)


print(isPalindrome('anna'), 'expected True')
print(isPalindrome('malayalam'), 'expected True')
print(isPalindrome('malayakam'), 'expected False')

def isPalindromeIter(s):
    ''' Check is string is palindrome iteratively'''
    if not s:
        return True
    for i in range(len(s) // 2):
        if s[i] != s[-1-i]:
            return False
    return True

print(isPalindromeIter('anna'), 'expected True')
print(isPalindromeIter('malayalam'), 'expected True')
print(isPalindromeIter('malayakam'), 'expected False')