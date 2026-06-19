# Arrays & Hashing
# Use Set data structure to store unique elements and have very fast (O(1)) lookup times

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        seenNumber = set()
        for i in range (len(nums)):
            if nums[i] in seenNumber: 
                return True
            else: 
                seenNumber.add(nums[i])
        return False
        