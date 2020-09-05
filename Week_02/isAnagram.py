class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s) == sorted(t)
        dc = collections.Counter(s)
        for k in t:
            dc[k] -= 1
        for _,v in dc.items():
            if v != 0:
                return False
        return True