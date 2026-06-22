# LC - Q35 - Easy 
# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity

### Wrong solution (only passed 44/66 test cases)
class Solution: 
    def searchInsertPosition(self, nums: List[int], target: int) -> int: 
        left = 0 
        right = len(nums) - 1

        while left < right: 
            mid = (left + right) // 2
            for i in range (len(nums)):
                if nums[i] == target: 
                    return i 
                elif nums[i] > target: 
                    right = mid
                elif nums[i] < target and nums[right] > target: 
                    left = mid 
                elif nums[i] < target and nums[right] < target: 
                    return right+1
            return mid
        
sol = Solution()
print(sol.searchInsertPosition([1,3,5,6], 5))
print(sol.searchInsertPosition([1,3,5,6], 2))
print(sol.searchInsertPosition([1,3,5,6], 7))

##################################################################
### Correct solution 
class Solution1: 
    def searchInsert(self, nums: List[int], target: int) -> int: 
        left = 0 
        right = len(nums) - 1

        while left <= right: 
            mid = (left + right) // 2
            if nums[mid] == target: 
                return mid 
            elif nums[mid] < target: 
                left = mid + 1
            else: 
                right = mid - 1
            
        return left 
sol = Solution1()
print("-----")
print(sol.searchInsert([1,3,5,6], 5))
print(sol.searchInsert([1,3,5,6], 2))
print(sol.searchInsert([1,3,5,6], 7))