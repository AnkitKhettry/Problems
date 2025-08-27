"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5

Constraints:
-1000 <= a, b <= 1000
"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        if a < b:
            # a should be the larger of the two
            a, b = b, a

        return self.convert_to_int(
            self.add_reverse_binaries(
                self.convert_to_reverse_binary(a), self.convert_to_reverse_binary(b)
            )
        )

    def convert_to_reverse_binary(self, x):
        bin_str = ""
        while x > 0:
            bin_str = bin_str + str(x % 2)
            x = int(x / 2)
        return bin_str
        # 11
        # 001

    def add_reverse_binaries(self, str1, str2):

        # str1 is always bigger than str2
        diff_len = len(str1) - len(str2)
        # Appending zeroes to str2 to make both strings of the same length
        for i in range(diff_len):
            str2 = str2 + "0"

        # 0, 0, 0 -> 0, 0
        # 1, 0, 0 -> 1, 0
        # 1, 1, 0 -> 0, 1
        # 1, 1, 1 -> 1, 1

        sum = ""
        carry_digit = 0
        for i in range(len(str1)):
            num_1s = int(str1[i]) + int(str2[i]) + carry_digit
            if num_1s == 0:
                next_digit = "0"
                carry_digit = 0
            elif num_1s == 1:
                next_digit = "1"
                carry_digit = 0
            elif num_1s == 2:
                next_digit = "0"
                carry_digit = 1
            elif num_1s == 3:
                next_digit = "1"
                carry_digit = 1
            sum = sum + next_digit

        sum = sum + str(carry_digit)
        return sum

    def convert_to_int(self, bin_str):
        sum = 0
        for i, ch in enumerate(bin_str):
            sum = sum + int(ch) * pow(2,i)
        return sum


if __name__ == "__main__":
        s = Solution()
        print(s.convert_to_reverse_binary(2))
        print(s.convert_to_reverse_binary(3))
        print(s.add_reverse_binaries(s.convert_to_reverse_binary(3), s.convert_to_reverse_binary(2)))
        print(s.getSum(2, 3))


