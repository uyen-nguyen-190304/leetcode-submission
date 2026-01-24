class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Record the numbers in spiral order
        res = []

        while matrix:
            # 1. Append elements of first row
            res += matrix.pop(0)

            # 2. Append last element of all rows
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())

            # 3. Append the last row in reverse order
            if matrix:
                res += (matrix.pop()[::-1])

            # 4. Append the first element of all lists in reverse order
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))

        # Return such order
        return res