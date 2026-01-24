class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Array to hold the return answer
        ret = []

        # Sort the array in ascending order
        nums_sorted = sorted(nums)

        # Loop through the sorted version to count smaller number than current
        hash_map = {}
        for i, v in enumerate(nums_sorted):
            if v not in hash_map:
                hash_map[v] = i

        # Translate that to the original array
        for _, k in enumerate(nums):
            ret.append(hash_map[k])

        # Return such answer
        return ret