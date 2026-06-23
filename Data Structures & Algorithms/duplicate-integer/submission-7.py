class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
          if num in hashset:
            return True
          hashset.add(num)
        return False
      











        # hashset = set()
        # for n in nums:
        #     if n in hashset:
        #         return True
        #     hashset.add(n)
        # return False

        # return not(len(set(nums)) == len(nums))