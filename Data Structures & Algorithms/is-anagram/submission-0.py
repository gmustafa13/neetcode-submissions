class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if length is not equal it  should return false
        if len(s) != len(t):
            return False
        count = {}

        # loop source and count the char 
        for char in s:
            count[char] = count.get(char,0) +1

        #loop t and compaire them with count if found decreemnt it 
        for char in t:
            if char not in count:
                return False
            # if char found the -
            count[char] -=1
            
            # if exact char is matched then count will be 0 and remove char from map
            if count[char] == 0 :
                del count[char]

        return len(count)== 0

        