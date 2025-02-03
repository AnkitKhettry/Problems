"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.



Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.


Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
"""


class Solution(object):

    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_len = 0
        l = r = 0
        str_length = len(s)
        count_of_chars = {}
        while r < str_length:

            count_of_chars[s[r]] = count_of_chars.get(s[r], 0) + 1

            if (r - l + 1) - max(count_of_chars.values()) > k:
                count_of_chars[s[l]] = count_of_chars.get(s[l], 0) - 1
                l = l + 1
            else:
                max_len = max(max_len, r - l + 1)
            r = r + 1

        return max_len


if __name__ == "__main__":
    sol = Solution()
    assert sol.characterReplacement("ABAB", 2) == 4
    assert sol.characterReplacement("AABABBA", 1) == 4
    assert sol.characterReplacement(
        "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 4) == 7
