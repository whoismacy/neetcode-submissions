class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxx = 0
        mapp = {}

        for r in range(len(s)):
            mapp[s[r]] = mapp.get(s[r], 0) + 1

            while (r - l + 1) - max(mapp.values()) > k:
                mapp[s[l]] -= 1
                l += 1
            maxx = max(r - l + 1, maxx)
        return maxx
        