"""
You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""


def merge_alternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    i = j = 0
    size_w1 = len(word1)
    size_w2 = len(word2)
    next_word = ""

    while i < size_w1 and j < size_w2:
        if i == j:
            next_word += word1[i]
            i = i+1
        else:
            next_word += word2[j]
            j = j+1

    if i < size_w1:
        next_word += word1[i:size_w1]

    if j < size_w2:
        next_word += word2[j:size_w2]

    return next_word


if __name__ == "__main__":
    print(merge_alternately("abc", "pqr"))
    print(merge_alternately("", "pqr"))
    print(merge_alternately("abc", ""))
    print(merge_alternately("abcde", "pqr"))
    print(merge_alternately("abc", "pqrst"))
