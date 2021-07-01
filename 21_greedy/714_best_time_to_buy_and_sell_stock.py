def maxProfit(prices, fee):
    profit = 0
    answer = []
    min_price = sum(prices)
    for price in prices:
        min_price = min(min_price, price)
        if profit > sum(answer):
            answer.append(profit)
            profit = price - min_price - fee
        else:
            answer.append(profit)
            profit = 0
    return sum(answer)

print(maxProfit([1,3,7,5,10,3], 3))