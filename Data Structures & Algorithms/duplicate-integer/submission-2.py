class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        len_set_nums = len(set(nums))
        if len_nums == len_set_nums:
            return False
        else:
            return True