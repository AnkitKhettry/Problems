"""
Write a function that takes the binary representation of a positive integer and returns the number of
set bits it has (also known as the Hamming weight).


Example 1:
Input: n = 11
Output: 3

Explanation:
The input binary string 1011 has a total of three set bits.
"""


def reverseBits(n: int) -> int:
    new_num = 0
    for i in range(0, 32):
        new_num = new_num * 2 + n % 2
        n = int(n / 2)

    return new_num


if __name__ == '__main__':
    assert reverseBits(43261596) == 964176192
    assert reverseBits(2147483644) == 1073741822
