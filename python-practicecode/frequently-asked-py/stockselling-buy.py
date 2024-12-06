def maxiprofit(l):
    min_profit=l[0]
    max_profit=0
    for price in l[1:]:
        max_profit=max(max_profit,price-min_profit)
        min_profit=min(price,min_profit)
    return max_profit
print(maxiprofit([7,1,2,4,5,8]))    


