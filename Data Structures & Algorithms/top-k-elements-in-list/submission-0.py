class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       # iterate through the given array
       # save  the no of times each integar appear in a dict
       # re-organize the key, value pair to the count,value
       # append it to a new array, then sort
       # we don't want to return anything higher than length of k
       # so we run a while loop
       #
       # return the k elements
      n = len(nums)
      count = {}
      result = []
      for i in nums:
            count[i] = count.get(i, 0) + 1
    
      arr = []
      for num, cout in count.items():
        arr.append([cout, num])
      arr.sort()
      
      res = []
      while len(res) < k:
        res.append(arr.pop()[1])
      return res
        



      




