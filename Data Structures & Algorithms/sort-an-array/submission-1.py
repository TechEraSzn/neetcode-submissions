# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
      
      
    #   if len(nums) <= 1:
    #     return nums

    #   n = len(nums)
    #   mid = len(nums) // 2

    #   left = self.sortArray(nums[:mid])
    #   right = self.sortArray(nums[mid:])

    #   l = 0
    #   r = 0
    #   ans = []

    #   while l < len(left) or r < len[right]:
    #     if r >= len(right) or l < len(left) and left[l] < right[r]:
    #         ans.append(left[l])
    #         l += 1
    #     else:
    #         ans.append(right[r])
    #         r -= 1

    #   return ans
   
     



class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, left, right):

        result = []

        i = 0
        j = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result













































    #    # while either half still has nums left
    #     while l_idx < len(left) or r_idx < len(right):
    #         # if right half is exhausted OR (left half is not exhausted AND left num is less than right num)
    #         if r_idx >= len(right) or l_idx < len(left) and left[l_idx] < right[r_idx]:
    #             ans.append(left[l_idx])
    #             l_idx+=1
    #         # left half is not exhausted or right num < left num
    #         else:
    #             ans.append(right[r_idx])
    #             r_idx+=1

    #     return ans

      
      
    #   for i in range(nums):

    

      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        # n = len(nums)
        # for i in nums:
        #     if nums[i + 1] < nums[i]:
        #         nums[i], nums[i + 1] = nums[i + 1], nums[i]
        # return nums

   
   
   
   
   
   
  
    # def bubble_sort(arr):
    #     n = len(arr)
    #     flag = True
    #     while flag:
    #         flag = False
    #         for i in nums:
    #             if nums[i + 1] < nums[i]:
    #                 nums[i + 1], nums[i] = nums 
       
       
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #  left = 0
        #  right = len(nums) - 1
        
       
        #  while left <= right:
        #   if nums[left] > nums[right]:
        #    nums[left] = nums[right]
        #    nums[right] = nums[left]
        #    left += 1
        #    right -= 1
        

        #  return nums