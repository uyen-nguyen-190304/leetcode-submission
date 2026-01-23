class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Make a set version of the list
        nums_set = set(nums)

        # Check if the two lengths are equal
        if len(nums) == len(nums_set):
            return False
        return True
        