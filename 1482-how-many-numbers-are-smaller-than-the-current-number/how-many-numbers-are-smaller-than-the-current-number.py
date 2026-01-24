class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ret = []

        for _, v in enumerate(nums):
            counter = 0
            for _, k in enumerate(nums):
                if k < v:
                    counter += 1
            ret.append(counter)

        return ret