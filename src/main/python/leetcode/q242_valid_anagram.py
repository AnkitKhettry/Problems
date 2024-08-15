"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s = {}
        dict_t = {}
        # Initialize each string's dict for each character
        for ch in s:
            dict_s[ch] = dict_s.get(ch, 0) + 1
        for ch in t:
            dict_t[ch] = dict_t.get(ch, 0) + 1

        for ch in "abcdefghijklmnopqrstuvwxyz":
            if dict_s.get(ch, 0) != dict_t.get(ch, 0):
                return False
        return True


if __name__ == "__main__":
    assert Solution().isAnagram("anagram", "nagaram")
    assert not Solution().isAnagram("rat", "car")
