class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # For each element move into buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        # Return most frequent items from buckets
        most_frequent = []
        for frequency in range(len(buckets) - 1, 0, -1):
            for val in buckets[frequency]:
                if len(most_frequent) == k:
                    return most_frequent
                most_frequent.append(val)
        
        return most_frequent
