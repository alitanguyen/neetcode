# Arrays & Hashing
# What to remmember: Count occurrencesd safely (without crashing): 
# d[k] = d.get(k, 0) + 1

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        dictChar = {}
        for i in s: 
            dictChar[i] = dictChar.get(i, 0) + 1 
            # increase i's count by 1, starting from 0 if it's new
        
        for i in t: 
            if i not in dictChar or dictChar[i] == 0:
                return False
            dictChar[i] -= 1
        return True

# testing 
sol = Solution()

assert sol.isAnagram("racecar", "carrace") == True

assert sol.isAnagram("jam", "jar") == False

print("All tests passed")