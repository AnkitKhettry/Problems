"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""


"""
applepenapple_ 
tfffftfftfffft

["pen", "apple"]
"""


def word_break(s, wordDict):
    grid = [False] * (len(s)+1)
    grid[len(s)] = True

    # Traverse backwards in the string
    for i in range(len(s)-1, -1, -1):
        # Check with each word if s[i:] starts with it. If yes, assign it the value of grid at the end of the word in s
        for word in wordDict:
            if len(word) <= len(s)-i:
                if word == s[i:(i+len(word))]:
                    grid[i] = grid[i+len(word)]
                    if grid[i]:
                        break

    print(grid)
    return grid[0]


if __name__ == "__main__":
    assert word_break("applepenapple", ["apple", "pen"])
    assert not word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])
