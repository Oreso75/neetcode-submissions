class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers_checkoff = dict()
        for num in nums: 
            if num not in numbers_checkoff: 
                numbers_checkoff[num] = 1
            else: 
                numbers_checkoff[num] += 1
        
        for value in numbers_checkoff: 
            if numbers_checkoff[value] > 1: 
                return True 

        return False 
        

        



        #for int in nums: 
            #if nums.count(int) > 1: 
                #return True 
        
        #return False 