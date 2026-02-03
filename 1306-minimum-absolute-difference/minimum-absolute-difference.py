class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Array to hold the answer
        ans = []

        # Sort the arr in ascending order
        arr.sort()

        # Min absolute difference
        min_difference = 2 * 10**6

        # Loop over the array once
        for i in range(len(arr) - 1):
            # Calculate the current difference
            difference = arr[i + 1] - arr[i]

            # If current difference is smaller, set new min diff and reset the return arr
            if difference < min_difference:
                min_difference = difference
                ans = [[arr[i], arr[i + 1]]]

            # Elif equal, append to return arr
            elif difference == min_difference:
                ans.append([arr[i], arr[i + 1]])

        # Return such answer
        return ans