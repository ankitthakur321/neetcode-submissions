class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        len_set_nums = len(set(nums))
        if len_nums == len_set_nums:
            return False
        else:
            return True
        # has_dupl = False
        # prev_num = None
        # for num in nums:
        #     if prev_num and num == prev_num:
        #         has_dupl = True
        #         break
        #     else:
        #         prev_num = num
        
        # return has_dupl