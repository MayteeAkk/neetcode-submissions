class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for index in range(len(nums)):
            difference = target - nums[index]
            if difference in values:
                return [values[difference], index]
            values[nums[index]] = index 