# Rotated array, but find the minimum element.

# Input:  nums = [3, 4, 5, 1, 2]
# Output: 1

### Approach 1 (do not use binary search)
# class Solution: 
#     def findMin(self, nums: List [int]) -> int: 
#         min = nums[0]
#         for i in range (len(nums)): 
#             if nums[i] < min: 
#                 min = nums[i]
#         return min 

# sol = Solution()
# print(sol.findMin([3, 4, 5, 1, 2]))

#########################################################

### Approach 2 (use binary search)
class Solution: 
    def findMin(self, nums: List [int]) -> int: 
        left = 0
        right = len(nums) - 1

        while left < right: 
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1     
            else: 
                right = mid  

        return nums[left]
    
        
sol = Solution()
print(sol.findMin([3, 4, 5, 1, 2]))          # 1
print(sol.findMin([3, 4, 5, 6, 7, 1, 2]))    # 1
print(sol.findMin([3, 4, 5, 6, 7, 8, 9, 0, 1, 2]))  # 0
print(sol.findMin([1]))                       # 1 — edge case: single element
print(sol.findMin([2, 1]))                    # 1 — edge case: two elements
print(sol.findMin([1, 2, 3, 4, 5]))          # 1 — edge case: not rotated

# Note: right = mid: to narrow the search space from the right, while keeping mid because it could be the answer

