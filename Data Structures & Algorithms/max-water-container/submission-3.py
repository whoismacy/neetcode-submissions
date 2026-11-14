class Solution:
       # I'm thinking of two pointers both at the beginning
       # we move the forward pointer
       # that isn't going to work, what about a pointer
       # on both extreme ends?
       # after watching the solution I fully misinterpreted the problem
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            capacity = min(heights[r], heights[l]) * (r - l)
            res = max(capacity, res)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return res

