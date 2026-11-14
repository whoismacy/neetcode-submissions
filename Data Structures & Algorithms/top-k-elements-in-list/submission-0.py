class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for element in nums:
            d[element] = d.get(element, 0) + 1
        sorted_elements = sorted(d.items(), reverse=True, key= lambda item: item[1])[:k]
        return [item[0] for item in sorted_elements]
