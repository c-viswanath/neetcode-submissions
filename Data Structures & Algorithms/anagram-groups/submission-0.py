class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for i in strs:
            x = "".join(sorted(i))
            if x not in hashMap:
                hashMap[x] = [i]
            else:
                hashMap[x].append(i)    
        return list(hashMap.values())                