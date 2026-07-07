class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #booyer's moore algorithm
        # count = 0
        # candidate = None
        # for num in nums:
        #     if count == 0:
        #         candidate = num
        #     if num == candidate:
        #         count += 1
        #     else:
        #         count -= 1
        # return candidate

        count = Counter(nums)
        res = []

        for key in  count:
            if count[key] > len(nums) // 3:
                res.append(key)
        return res
            
        
        