class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Two pointers: i for negative, j for positive
        j = 0
        while j < len(nums):
            if nums[j] < 0:
                j = j + 1
            else:
                break
        i = j - 1

        # Array to hold the answer
        ans = []

        # Append in increasing squaring order
        while (i >= 0) and (j < len(nums)):
            if abs(nums[i]) < nums[j]:
                ans.append(nums[i]**2)
                i = i - 1
            else:
                ans.append(nums[j]**2)
                j = j + 1

        # Append the rest
        while (i >= 0):
            ans.append(nums[i]**2)
            i = i - 1
        while (j < len(nums)):
            ans.append(nums[j]**2)
            j = j + 1

        # Return the sorted square array
        return ans