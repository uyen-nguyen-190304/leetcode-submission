class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        checking_window = set()
        for i, v in enumerate(nums):
            if v in checking_window:
                return True
            checking_window.add(v) # right end
            if len(checking_window) > k:
                checking_window.remove(nums[i - k]) # left end
        return False