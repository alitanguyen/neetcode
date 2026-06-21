class Solution: 
    def smallestNum (self, nums: List[int]):
        minNum = nums[0]
        for i in range (len(nums)-1):
            if minNum > nums[i+1]:
                minNum = nums[i+1]
        return minNum

sol = Solution()
print(sol.smallestNum(nums = [3, 4, 6, 2, 1])) 
