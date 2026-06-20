# Stack

# logic flow: 
# check if close bracket matches open bracket in the hash map => yes => pop it out 
# stack is empty => all matches in the correct order => return true 

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpenPairs = {"]":"[","}":"{", ")":"("}

        for char in s: 
            if char in closeToOpenPairs:
                # check if stack is not empty & does the top match what we need
                if stack and stack[-1] == closeToOpenPairs[char]:
                    stack.pop()
                else:  
                    return False
            else: 
                stack.append(char)
        return True if not stack else False 

sol = Solution()
assert sol.isValid(s = "([{}])") == True
assert sol.isValid(s = "[(])") == False

print("All tests are passed")
