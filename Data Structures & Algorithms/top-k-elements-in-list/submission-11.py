class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = [[] for i in range(len(nums) + 1)]
        # counter = Counter(nums)
        # res = []
        # for key, val in counter.items():
        #     freq[val].append(key)
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res
        counter = Counter(nums)
        freq = []
        for n,i in counter.items():
            freq.append([-i,n])
        heapq.heapify(freq)
        res = []
        for i in range(k):
            ind,n = heapq.heappop(freq)
            res.append(n)
        return res