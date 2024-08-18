"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3, Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        size = len(s)
        if size % 2 != 0:
            return False

        p_dict = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []
        stack_len = 0
        for ch in s:
            if stack_len > 0 and stack[stack_len-1] == p_dict.get(ch, "d"):
                stack.pop()
                stack_len -= 1
            else:
                stack.append(ch)
                stack_len += 1

        if stack_len == 0:
            return True
        return False


if __name__ == "__main__":
    assert Solution().isValid("()")
    assert Solution().isValid("()[]{}")
    assert not Solution().isValid("(]")
