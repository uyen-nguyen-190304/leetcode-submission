class Solution:
    def rob(self, nums: List[int]) -> int:
        # Create a 1D DP array
        OPT = [0] * (len(nums) + 1)

        # Base case
        OPT[1] = nums[0]

        # Recursive
        for i in range(2, len(nums) + 1):
            OPT[i] = max(nums[i - 1] + OPT[i - 2], OPT[i - 1])

        return OPT[len(nums)]