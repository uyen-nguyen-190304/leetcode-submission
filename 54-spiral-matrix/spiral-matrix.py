class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Helper function
        def tranversal_check():
            # Check if we have already finish the spiral tranversal 
            if len(matrix) == 0:
                return True

        # Record the numbers in spiral order
        res = []

        while True:        
            # Step 1: Append elements of the first non-empty list
            res.extend(matrix[0])
            matrix.pop(0)

            if tranversal_check():
                return res

            # Step 2: Append the last element of all lists in order
            for col in matrix:
                res.append(col[-1])
                col.pop(-1)
            
            matrix = [item for item in matrix if len(item) > 0]

            if tranversal_check():
                return res

            # Step 3: Append the reverse of the last list
            res.extend(matrix[-1][::-1])
            matrix.pop(-1)

            if tranversal_check():
                return res

            # Step 4: Append the first element of the remaining list in reverse order
            for col in reversed(matrix):
                res.append(col[0])
                col.pop(0)
            
            matrix = [item for item in matrix if len(item) > 0]

            if tranversal_check():
                return res
    