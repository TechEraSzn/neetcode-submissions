class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sort = set(nums)
        longest = 0
        for num in sort:
            if (num - 1) not in sort:
                length = 1
                while (num + length) in sort:
                    length += 1
                longest = max(length, longest)


        return longest









            