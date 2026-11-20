class Solution:
    def reverseBits(self, n: int) -> int:
        #result = []
        binary_n = bin(n)[2:].zfill(32)
        reversed_bin = binary_n[::-1]
        #for num in reversed_bin_list:
            #result.append(num)
        #result = "".join(map(str,reversed_bin_list))

        real_number = int(reversed_bin, 2)
        
        return real_number
