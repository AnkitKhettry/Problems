"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

abcde
gapdef

    " a b c d e
"   0 0 0 0 0 0
g   0 0 0 0 0 0
a   0 1 1 1 1 1
p   0 1 1 1 1 1
d   0 1 1 1 2 2
e   0 1 1 1 2 3
f   0 1 1 1 2 3


    " a c a
"   0 0 0 0
d   0 0 0 0
a   0 1 1 1
b   0 1 1 1
c   0 1 2 2

"""


def lcs(text1, text2):
    lcs_grid = [[0] * (len(text2)+1) for i in range(len(text1)+1)]

    for i in range(1, len(text1)+1):
        for j in range(1, len(text2)+1):
            if text1[i-1] == text2[j-1]:
                lcs_grid[i][j] = lcs_grid[i-1][j-1]+1
            else:
                lcs_grid[i][j] = max(lcs_grid[i - 1][j], lcs_grid[i][j-1])

    return lcs_grid[len(text1)][len(text2)]


if __name__ == "__main__":
    assert lcs("abcde", "ace") == 3
    assert lcs("dabc", "ace") == 2


