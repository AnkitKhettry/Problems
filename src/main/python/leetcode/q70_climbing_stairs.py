"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""


def climb_stairs(n):
    # For n=1 and 2, the number of ways to climb are 1 and 2 respectively.
    if n == 1:
        return 1
    if n == 2:
        return 2
    p1, p2 = 1, 2
    new_ways = 0
    for i in range(3, n + 1):
        new_ways = p1 + p2
        p1 = p2
        p2 = new_ways

    return new_ways


if __name__ == "__main__":
    assert climb_stairs(2) == 2
    assert climb_stairs(4) == 5
