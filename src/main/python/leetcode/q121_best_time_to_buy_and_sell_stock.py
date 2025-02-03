"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""


def max_profit(prices):
    # Dry run with [7,3,5,1,4,6,2]
    max_profit = 0
    curr_buy = prices[0]

    for price in prices[1:]:
        if price < curr_buy:
            curr_buy = price
        else:
            max_profit = max(price - curr_buy, max_profit)
    return max_profit


if __name__ == "__main__":
    assert max_profit([2, 3, 1, 3, 6, 4]) == 5
    assert max_profit([6, 5, 4, 3, 2, 1]) == 0
    assert max_profit([7, 3 ,5, 1, 4, 6, 2]) == 5
