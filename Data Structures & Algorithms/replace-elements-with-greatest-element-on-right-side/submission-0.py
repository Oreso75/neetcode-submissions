class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        k = 0 
        for num in arr:
            max_num = 0  
            for i in range (k + 1, len(arr)): #from the next index in arr until the end
                if arr[i] > max_num: 
                    max_num = arr[i]
            arr[k] = max_num
            k += 1
        
        arr[-1] = -1

        return arr
        