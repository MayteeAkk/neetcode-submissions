class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        result = []

        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        # Now we have freqency values

        for key, value in freq_map.items():
            buckets[value].append(key)

        for index in range (len(buckets) - 1, 0, -1):
            if buckets:
                for num in buckets[index]:
                    result.append(num)
                if len(result) == k:
                    return result
