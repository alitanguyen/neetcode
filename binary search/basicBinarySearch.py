# Given a sorted array and a target, return the index. Return -1 if not found.

# Input:  nums = [-1, 0, 3, 5, 9, 12],  target = 9
# Output: 4

# Only applied for sorted list
class Solution: 
    def binarySearch(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1


        while left <= right: 
            mid = (left + right) // 2 
            if nums[mid] == target: 
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else: 
                left = mid + 1
        return -1 


sol = Solution() 
print(sol.binarySearch([-1, 0, 3, 5, 9, 12], 9)) 