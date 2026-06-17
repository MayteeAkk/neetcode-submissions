class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range((len(nums) + 1))] 
        frequency_map = dict()
        result = []

        for num in nums: 
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1
        
        for key, value in frequency_map.items():
            bucket[value].append(key)

        for index in range(len(bucket) - 1, 0, -1):
            if bucket[index]:
                for num in bucket[index]:
                    result.append(num)

            if len(result) == k:
                return result
