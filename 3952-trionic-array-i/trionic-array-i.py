class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        p = 0
        n = len(nums)
        # Increasing part
        while p < n - 1 and nums[p] < nums[p + 1]:
            p = p + 1
        
        if p == 0 or p >= n - 2:
            return False
    
        # Decreasing part
        q = p
        while q < n - 1 and nums[q] > nums[q + 1]:
            q = q + 1
        
        if p == q or q >= n - 1:
            return False
        
        # Increasing part
        while q < n - 1:
            if nums[q] >= nums[q + 1]:
                return False
            q = q + 1
        return True

