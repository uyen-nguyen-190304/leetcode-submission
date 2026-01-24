class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(len(points) - 1):
            current_point = points[i]
            next_point = points[i + 1]
            
            diff1 = abs(current_point[0] - next_point[0])
            diff2 = abs(current_point[1] - next_point[1])

            time += min(diff1, diff2) + abs(diff1 - diff2)

        return time