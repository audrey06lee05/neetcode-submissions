class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared = set()
        for i in nums:
            if i not in appeared:
                appeared.add(i)
            else: return True
        return False