class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        d=Counter(nums)
        for i in nums:
            if d[i]>1:
                return True
        return False