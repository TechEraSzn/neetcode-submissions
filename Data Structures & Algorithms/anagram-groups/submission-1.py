class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # i want to iterate through each string
        # I also want to sort each word
        # then create a sublit for each sorted word but in their own word
        # return the sub array
       hashmap = {}
       for i in strs:
        sorty = "".join(sorted(i))
        if sorty not in hashmap:
          hashmap[sorty] = []
        hashmap[sorty].append(i)
       return list(hashmap.values())

