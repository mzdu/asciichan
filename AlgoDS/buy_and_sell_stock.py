prices = [6,5,4,3,2,1]
prices2 = [7,1,5,3,6,4]

def maxProfit(prices):
    profit, smallest = 0, prices[0]
    for i in xrange(1, len(prices)):
        # if current price is less than smallest, it could be a potential buy point
        if prices[i] < smallest:
            # no need to calculate profit, just update smallest
            smallest = prices[i]
        # found potential sell point
        else:
            # check the potential profit, if it is greater than existing profit
            # update it
            if prices[i] - smallest > profit:
                profit = prices[i] - smallest
    return profit

print maxProfit(prices2)


