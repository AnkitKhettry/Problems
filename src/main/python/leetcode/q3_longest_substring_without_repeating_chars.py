"""
Given a string s, find the length of the longest
substring
 without repeating characters.

Example:

Input: s = "abcbacbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""


def length_of_longest_substring_bruteforce(s):
    max_length = 0
    for i in range(len(s)):
        set_of_chars = set()
        j = i
        while j < len(s) and s[j] not in set_of_chars:
            set_of_chars.add(s[j])
            j = j+1
        max_length = max(max_length, j - i)

    return max_length


def length_of_longest_substring(s):
    left = 0
    right = 0
    max_length = 0
    current_char_set = set()

    # Sliding window
    while right < len(s):
        # At any time, no character is added twice to the set.
        # If a duplicate character is found, start removing characters from the left.
        # Solution explanation: https://www.youtube.com/watch?v=wiGpQwVHdE0
        while s[right] in current_char_set:
            current_char_set.remove(s[left])
            left = left + 1
        current_char_set.add(s[right])
        right = right+1
        max_length = max(max_length, right - left)

    return max_length


if __name__ == "__main__":
    print(length_of_longest_substring("abcbcdeb"))
