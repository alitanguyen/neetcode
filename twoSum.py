# What to remmember: 
# for i, n in enumerate(nums): → index + value

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate (nums):
            complement = target - n
            if complement in seen: 
                return [seen[complement], i]
            seen[n] = i
        return []

sol = Solution()

print(sol.twoSum([2, 7, 11, 15], 9))   
print(sol.twoSum([3, 2, 4], 6))         
print(sol.twoSum([1, 5, 3, 7], 8))     


