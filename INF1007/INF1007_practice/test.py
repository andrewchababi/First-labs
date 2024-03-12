class Solution:
    def binarySearch(self, nums: list[int], target: int, start: int, end: int) -> int:
        if not nums:
            return 0 
        elif len(nums) == 1:
            if target <= nums[0]:
                return 0 
            else:
                return 1
        
        if start == end-1:
            if target > nums[end]:
                return end+1
            elif target <= nums[start]:
                return start
            else:
                return end
                

        mid = (end-start+1)//2
        if nums[start + mid] == target:
            return mid
        elif nums[start + mid] < target:
            return self.binarySearch(nums, target, start+mid, end)
        elif nums[start + mid] > target:
            return self.binarySearch(nums, target, start, start + mid)


    def searchInsert(self, nums: list[int], target: int) -> int:
        return self.binarySearch(nums, target, 0 , len(nums) - 1 )


    

        