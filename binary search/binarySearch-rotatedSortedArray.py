# A sorted array was rotated at some pivot. Find the target. (classic interview)

# Input:  nums = [4, 5, 6, 7, 8, 0, 1, 2],  target = 8 
# Output: 4

class Solution: 
    def binarySearch(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)-1

        while left <= right: 
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else: 
                    left = mid + 1
            
            # right half is sorted
            else: 
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else: 
                    right = mid - 1

sol = Solution() 
print(sol.binarySearch([4, 5, 6, 7, 8, 0, 1, 2], 8)) 






