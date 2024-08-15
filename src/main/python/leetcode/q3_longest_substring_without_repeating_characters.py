"""
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        size = len(s)
        currset = set()
        i = 0
        j = 0

        max_size = 0

        while j < size:
            if s[j] in currset:
                while s[i] != s[j]:
                    currset.remove(s[i])
                    i = i + 1
                i = i + 1
            currset.add(s[j])
            max_size = max(max_size, j - i + 1)
            j = j + 1

        return max_size


if __name__ == "__main__":
    s = "abcabcbb"
    assert Solution().lengthOfLongestSubstring(s) == 3
