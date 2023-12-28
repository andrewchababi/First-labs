class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            if target > nums[0]:
                return 1
            else:
                return 0


        start_pointer = 0
        end_pointer = len(nums) -1 
        is_done = False

        while not is_done:
            mid_pointer = (end_pointer + start_pointer) // 2

            if mid_pointer == target:
                return mid_pointer
            
            if nums[mid_pointer] > target:
                end_pointer = mid_pointer - 1

            else:
                start_pointer = mid_pointer + 1

