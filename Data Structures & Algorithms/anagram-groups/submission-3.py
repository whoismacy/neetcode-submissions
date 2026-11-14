class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        vals = {}
        for val in strs:
            vals.setdefault(tuple(sorted(val)), []).append(val)
        return list(vals.values())