# Two Pointers
# What to remmember? 
# 1. how to lowercases the given string, deletes all spaces, keep letters only 
# 2. how to use two pointers

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lowercases the given string, deletes all spaces, keep letters only 

        newS = "".join(filter(str.isalnum, s.lower()))
        # isalnum without () - why? 
        # because we're handing the method itself to filter(), and filter() will call it on each character


        # two pointers
        left = 0 
        right = len(newS) - 1

        while left < right: 
            if newS[left] != newS[right]:
                return False
            left += 1
            right -= 1
        
        return True

sol = Solution()
assert sol.isPalindrome ("Is it a cat?") == False
assert sol.isPalindrome("Was it a car or a cat I saw?") == True

print("All tests passed")