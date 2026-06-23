class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {} 
        for i in strs:
            sort = "".join(sorted(i))
            if sort not in hashtable:
                hashtable[sort] = []
            hashtable[sort].append(i)
        return list(hashtable.values())
            
            
                
            
        