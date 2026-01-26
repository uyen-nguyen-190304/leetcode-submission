class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            # Know what we need to search for the second one
            needed = target - numbers[i]

            # Binary search
            left = i + 1
            right = len(numbers) - 1
            while left <= right:
                middle = (left + right) // 2
                # If found such
                if numbers[middle] == needed:
                    # Added by one as required
                    return [i + 1, middle + 1]
                elif needed < numbers[middle]:
                    right = middle - 1
                else:
                    left = middle + 1

        # Just for defensive
        return [None, None]