class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        #close_points = []
        for i in points:
           curr_dist = i[0]*i[0]+i[1]*i[1]
           #close_points.append([i,curr_dist])
           i.append(curr_dist)
        #print(points)
        points.sort(key = lambda x : x[2])
        return [[x[0],x[1]] for x in points[:k] ]