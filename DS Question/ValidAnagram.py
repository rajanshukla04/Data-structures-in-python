"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once."""


'''Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false'''

def ValidAnagram(s,t):
    if len(s)!=len(t):
        return False
    text=[0]*26
    patt=[0]*26

    for i in range(len(s)):
        text[ord(s[i])-97]+=1
        patt[ord(t[i])-97]+=1
    if text==patt:
        return True
    return False


s = "anagram"
t = "nagaram"

print("The string are Anagram ? ")
print(ValidAnagram(s,t))


