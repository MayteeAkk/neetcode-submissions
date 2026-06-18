class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp_array = nums.copy()
        for num in nums:
            temp_array.append(num)

        return temp_array