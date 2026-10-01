"""
NO extra space


o(n2)
loop tr
two pointer
both the pointer moving in same direction
"""
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        i1 = 0
        i2 = len(numbers)-1
        while i1<i2:
            if  numbers[i1]+numbers[i2] == target:
                return [i1+1, i2+1]
            elif numbers[i1]+numbers[i2] < target:
                i1+=1
            else:
                i2-=1
                

        