from typing import List

class BestTimeToBuyAndSellStock:
    """
        121. Best Time to Buy and Sell Stock

        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    """
    def maxProfit(self, prices: List[int]) -> int:
        """
            O(n), two pointer solution, we place left at the beginning and right at index 1,
            then in each iteration we calculate the profit, move right and if the value at left is greater than value at right
            then we put left at right
        """
        if len(prices) <= 1:
            return 0

        left = 0
        right = 1

        max_profit = 0
        while left < right and right < len(prices):
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)

            if prices[left] >= prices[right]:
                left = right
                
            right += 1
        
        return max_profit

    def max_profit_brute_force(self, prices: List[int]) -> int:
        """
            O(n^2), try every combination
            solves the problem but fails due to timeout in leetcode
        """
        max_profit = 0
        for idx, buy_price in enumerate(prices):
            for sell_price in prices[idx+1:]:
                max_profit = max(max_profit, sell_price - buy_price)

        return max_profit


if __name__ == '__main__':
    object = BestTimeToBuyAndSellStock()

    print(object.maxProfit([7,1,5,3,6,4])) # 5
    print(object.maxProfit([7,6,4,3,1])) # 0
    print(object.maxProfit([2,1,4])) # 3
    print(object.maxProfit([2,1,2,1,0,1,2])) # 2
    print(object.maxProfit([1,2,4,2,5,7,2,4,9,0,9])) # 9