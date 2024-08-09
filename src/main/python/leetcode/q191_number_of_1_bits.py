"""
Write a function that takes the binary representation of a positive integer and returns the number of
set bits it has (also known as the Hamming weight).


Example 1:
Input: n = 11
Output: 3

Explanation:
The input binary string 1011 has a total of three set bits.
"""


def hamming_weight(n):
    num_ones = 0
    while n > 0:
        num_ones = num_ones + (n % 2)
        n = int(n / 2)

    return num_ones


if __name__ == '__main__':
    assert hamming_weight(11) == 3
    assert hamming_weight(128) == 1
