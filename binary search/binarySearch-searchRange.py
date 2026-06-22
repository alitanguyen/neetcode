# LC - Q34 - Medium 
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

### Wrong answer (only passed 28/88 test cases) 
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: 
            return [-1, -1]
        
        left = 0
        right = len(nums) - 1

        if nums[left] == nums[right] == target:
            return [0, 1]

        while left < right: 
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
                mid2 = (left + right) // 2
                if nums[mid2] == target:
                     
                    return [left, mid2]
                else: 
                    return [-1, -1]  
            else: 
                right = mid - 1
                mid2 = (left + right) // 2
                complement = nums[mid2] - target
                if nums[mid2] == target:
                    return [mid2, right]
                else: 
                    return [-1, -1]  

        return [-1, -1] 

sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8))
print(sol.searchRange([5,7,7,8,8,10], 6))
print(sol.searchRange([], 0))
print(sol.searchRange([1,2,2,7,8,8,8],2))
print(sol.searchRange([8,8],8))