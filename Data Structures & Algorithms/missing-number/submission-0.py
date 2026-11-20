class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        list_of_nums = set()
        for i in range(len(nums)+1):
            list_of_nums.add(i)
        for num in list_of_nums: 
            if num not in nums: 
                return num 

