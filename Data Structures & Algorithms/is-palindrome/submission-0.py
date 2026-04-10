'''
1. lower the characters
2. remove the space and the all non-alphanumeric characters
3. remove space
4. two pointer meet in middle or crosses one another then True else False

'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=(''.join([_ for _ in s if _.isalnum()])).lower()
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1

        return True
        