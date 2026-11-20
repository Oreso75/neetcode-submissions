class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #for price in prices:
        potential_profits = []
        for i in range(len(prices)): 
            price = prices[i]
            for num in prices[i+1:]:    
                if num > price: 
                    diff = num - price 
                    potential_profits.append(diff)

                #if there is a number from price to end of prices: 
                    #subtract that number from price 
                    #put these numbers in a list 
                    #sort the list and index to -1 to get highest value

        if len(potential_profits) == 1: 
            return int(sorted(potential_profits)[0])
        elif potential_profits == []:
            return 0 
        else: 
            return int(sorted(potential_profits)[-1])