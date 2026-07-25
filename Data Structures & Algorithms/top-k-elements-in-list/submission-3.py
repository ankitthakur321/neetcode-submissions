from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [key for key, _ in sorted(count.items(), key=lambda item: item[1], reverse=True)[:k]]