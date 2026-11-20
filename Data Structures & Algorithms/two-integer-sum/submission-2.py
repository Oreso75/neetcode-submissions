class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_hash = dict()
        for index, num  in enumerate(nums):
            diff = target - num
            if diff in number_hash: 
                nums_pair = [number_hash[diff], index]
                return nums_pair
            number_hash[num] = index
            

        return sorted(nums_pair)

            