def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    result = 0
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if prices[j] - prices[i] > result:
                result = prices[j] - prices[i]
    return result

'''
이렇게 브루트 포스로 계산하면 타임아웃이다.
저점과 현재 값과의 차이를 계속 업데이트해가는 방식으로 풀 수 있다.
'''

def maxProfit2(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    lowpoint = prices[0]
    result = 0
    for i in range(len(prices)):
        if prices[i] - lowpoint > result:
            result = prices[i] - lowpoint
        if prices[i] < lowpoint:
            lowpoint = prices[i]

    return result

import sys
def maxProfit3(self, prices):
    profit = 0
    min_price = sys.maxsize
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price-min_price)
    return profit