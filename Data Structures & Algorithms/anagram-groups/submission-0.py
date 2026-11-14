class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        vals = {}
        for val in strs:
            new_val = str(sorted(val))
            vals.setdefault(new_val, []).append(val)
        return list(vals.values())