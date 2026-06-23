class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for num in nums: # or for num in range(len(nums))
          if num != val:
            nums[k] = num # or nums[k] = nums[num]
            k += 1
        return k


