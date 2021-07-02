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

print('---Group anagrams---')
words =  ["yoo", "act", "bar", "tac", "foo", "cat", "oyo", "arb"]
print(groupAnagrams(words))
words = ['act']
print(groupAnagrams(words))
    



def strStr(self, haystack: str, needle: str) -> int:
    '''
    Find a needle in a haystack or strstr.
    Return the index of the first occurence of needle string within the haystack string

    hello   ll
        ^
        ^
        return i pointer 

        cases:
        needle found -> return index of first letter
        empty needle -> return 0
        needle not found -> return -1
    
    '''
    if not needle:
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                break
            if j == len(needle) - 1:            # if reached the end of needle
                return i
            
    return -1

def reverseWordsInString(s):
    return ' '.join(reversed(s.split()))

print('---Reversing words in string---')
print(reverseWordsInString('it is a beautiful day'), 'expected: day beautiful a is it')
print(reverseWordsInString(' i'))

def lengthOfLongestSubstring(s):
    if not s:
        return 0
    max_substr = 1
    left = 0
    chars = set()
    for right in range(len(s)):
        while s[right] in chars:
            chars.discard(s[left])
            left += 1
        chars.add(s[right])
        max_substr = max(max_substr, right - left + 1)

    return max_substr

print('---Length of longest substring without repeating characters---')
s = "abcabcbb"
print(lengthOfLongestSubstring(s), 'expected 3')
s = "bbbb"
print(lengthOfLongestSubstring(s), 'expected 1')
s = ""
print(lengthOfLongestSubstring(s), 'expected 0')

