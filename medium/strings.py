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


def groupAnagrams(words):
    'Giver a list of strings, return a list of grouped anagrams (strings that have the same characters regardless of order)'
    ref = {}
    for word in words:
        sorted_word = ''.join(sorted(word ))
        if sorted_word in ref:
            ref[sorted_word].append(word)
        else:
            ref[sorted_word] = [word]
    return list(ref.values())

    words =  ["yoo", "act", "bar", "tac", "foo", "cat", "oyo", "arb"]
    print(groupAnagrams(words))
    words = ['act']
    print(groupAnagrams(words))
    