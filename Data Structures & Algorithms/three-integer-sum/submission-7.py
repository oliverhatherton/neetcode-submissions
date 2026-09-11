class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums) - 2):
            seen = set()
            for j in range(i + 1, len(nums)):
                complement = -(nums[i] + nums[j])
                if complement in seen:
                    res.add(tuple(sorted((nums[i], nums[j], complement))))
                seen.add(nums[j])
        return [list(t) for t in res]