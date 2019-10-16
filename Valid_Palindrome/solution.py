class Solution(object):
    def isPalindrome(self, s):
        i = 0 
        j = len(s) - 1 
        while i < j:
            right = s[i]
            left = s[j]
            if not right.isalnum():
                i +=1
                continue
            elif not left.isalnum():
                j -=1
                continue
            elif right.lower() != left.lower():
                return False
            i +=1
            j -=1
        return True

