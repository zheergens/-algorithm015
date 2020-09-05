class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ds = dict()
        for x in strs:
            y = ''.join(sorted(x))
            if y in ds:
                ds[y].append(x)
            else:
                ds[y] = [x]
        return [v for _, v in ds.items()]
        