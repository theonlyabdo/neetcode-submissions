class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        
        sorted_freq = sorted(freq.items(), key=lambda x: x[1])
        
        output = [item[0] for item in sorted_freq[-k:]]
        
        return output