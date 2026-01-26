class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Array to hold the answer
        ans = []

        # Sort the given array in ascending order
        nums.sort()

        # Loop through the list for first value, then find the other two
        for index, value in enumerate(nums[:-2]):
            if (index > 0) and (value == nums[index - 1]):
                continue
            
            left = index + 1
            right = len(nums) - 1
            while left < right:
                currentSum = value + nums[left] + nums[right]
                if currentSum > 0:
                    right = right - 1
                elif currentSum < 0:
                    left = left + 1
                else:
                    ans.append([value, nums[left], nums[right]])
                    left += 1

                    while (left < right) and (nums[left] == nums[left - 1]):
                        left += 1

        # Return such answer
        return ans