'''
we can do this by binary seach
only challend it to get the index for row and column of the matrix

total = m*n
ex = 12
lp=0 and rp=11
mid = 5
now we do know n
row = 5//4 =1
column = 5%4=1 so smaller
lp=0 and rp =4 mid = 2
row = 2//4 = 0
column= 2
lp=0 and rp = 1 and mid =0
row= 0//4=0
column=0%2=0
now this is smaller 
lp=1 and rp =1 and mid =1
row=0, column=1 and the target is found

'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        m = len(matrix)
        lp=0
        rp= (m*n)-1
        while lp<=rp:
            mid = lp+(rp-lp)//2
            row=mid//n
            col=mid%n
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                rp=mid-1
            else:
                lp=mid+1
        return False

        