#Algoithm: 
#     => create two pointers i and j where i will point to the first element in the string,
#        and j will point to the last one.
#     => scan from right and left, if both elements at i and j are alphanumeric chars,
#        and equal to each other, increment i and decrement j. 
#     => if any of the elements is not alphanumeric, increment i if it is right, decrement j if it is left,
#        and continue (without checking equality) scanning till both chars are alphanumeric. 
#     => if both chars are alphanumeric and are not equal, return false. 
#     => if i == j or j < i, which means that the two pointers met without finding any unequal chars, return true.
    


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

