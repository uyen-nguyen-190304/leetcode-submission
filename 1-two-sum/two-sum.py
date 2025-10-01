class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            current = nums[i]
            need = target - current
            if need in hashTable:
                return (hashTable[need], i)
            else:
                hashTable[current] = i        
    