class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Convert to a set to eliminate duplicated values
        nums_set = set(nums)

        # Loop through and find missing values
        ans = []
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                ans.append(i)

        # Return the answer
        return ans
        
        