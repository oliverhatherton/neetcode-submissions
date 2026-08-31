class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        prefix = 1
        postfix = 1
        nums_len = len(nums)

        for i in range(nums_len):
            out.append(prefix)
            prefix *= nums[i]
        
        for j in range(nums_len - 1, -1, -1):
            out[j] *= postfix
            postfix *= nums[j]

        return out