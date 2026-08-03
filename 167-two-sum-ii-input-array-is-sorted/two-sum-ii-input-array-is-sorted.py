class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointers
        left = 0
        right = len(numbers) - 1

        # Problem guaranteed that there is a unique solution
        # Also not use the same element twice
        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left + 1, right + 1]
            elif current < target:
                left += 1
            else:
                right -= 1
        