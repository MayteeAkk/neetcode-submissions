class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Use Bucket Sort (because we have a limited and defined set of values in the array)
        buckets = [0] * 3
        for index in range(len(nums)):
            buckets[nums[index]] += 1
        
        i = 0
        for index in range(len(buckets)):
            for count in range(buckets[index]):
                nums[i] = index
                i += 1
        