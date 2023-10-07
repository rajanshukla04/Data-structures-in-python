"""You are given an array of prices where prices[i] is the price of a given
stock on an ith day. You want to maximise your profit by choosing a
single day to buy one stock and choosing a different day in the future to
sell that stock. Return the maximum profit you can achieve from this
transaction. If you cannot achieve any profit, return 0.
"""
def MaxProfit(prices):
    maxp=0
    minp=prices[0]
    for i in range(1,len(prices)):
        minp=min(minp,prices[i])
        profit=prices[i]-minp
        maxp=max(maxp,profit)
    return maxp


prices = [7,1,5,3,6,4]
print("Maximum Profit of  prices = [7,1,5,3,6,4]  :",MaxProfit(prices))

prices = [7,6,4,3,1]
print("Maximum Profit of  prices = [7,6,4,3,1] : ",MaxProfit(prices))