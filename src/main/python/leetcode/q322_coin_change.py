"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1
"""


def coin_change(coins, amount):
    min_coins = [amount+1] * (amount+1)
    min_coins[0] = 0
    for amt in range(1, amount+1):
        for coin in coins:
            if amt >= coin:
                min_coins[amt] = min(min_coins[amt], min_coins[amt-coin] + 1)

    print(min_coins)

    if min_coins[amount] < amount+1:
        return min_coins[amount]
    else:
        return -1


def coin_change_bad(coins, amount):
    min_coins = [[amount+1] * (amount + 1) for i in range(len(coins))]
    if amount == 0:
        return 0

    for i in range(len(coins)):
        min_coins[i][0] = 0

    for i in range(len(coins)):
        for j in range(1, amount + 1):
            if j < coins[i]:
                min_coins[i][j] = min_coins[i - 1][j]
                continue
            min_coins[i][j] = min(min_coins[i][j], min_coins[i - 1][j], min_coins[i][j - coins[i]] + 1)

    reqd_min_coins = min_coins[len(coins) - 1][amount]

    if reqd_min_coins == amount+1:
        return -1
    else:
        return reqd_min_coins


if __name__ == "__main__":
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([2147483647], 2) == -1
