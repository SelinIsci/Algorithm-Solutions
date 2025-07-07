class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {key: value for value, key in enumerate(nums)}

        for i in range(len(nums)):
            value = target - nums[i]
            if value in d and d[value] != i:
                return [d[value], i]
