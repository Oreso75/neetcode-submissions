class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        streak_list = []
        for num in nums: 
            if num == 1: 
                counter += 1
            else: 
                streak_list.append(counter)
                counter = 0 
            
        streak_list.append(counter)
        return sorted(streak_list)[-1]