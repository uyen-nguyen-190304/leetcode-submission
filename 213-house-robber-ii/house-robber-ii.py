class Solution:
    def rob(self, nums: List[int]) -> int:
        # Defensive check
        if not nums:
            return 0 
        # If only one house, return that
        n = len(nums)
        if n == 1:
            return nums[0]
        # If two houses, return the larger one
        if n == 2:
            return max(nums[0], nums[1])

        # Run 1: max from house 0 to house n-2
        nums1   = nums[:n-1]
        OPT1    = [0] * n
        OPT1[1] = nums1[0]
        for i in range(1, n):
            OPT1[i] = max(nums1[i - 1] + OPT1[i - 2], OPT1[i - 1])
        choice1 = OPT1[n - 1]

        # Run 2: max from house 1 to house n-1
        nums2    = nums[1:]
        OPT2     = [0] * n
        OPT2[1]  = nums2[0]
        for j in range(1, n):
            OPT2[j] = max(nums2[j - 1] + OPT2[j - 2], OPT2[j - 1])
        choice2  = OPT2[n - 1]

        # Return the better value
        return max(choice1, choice2)