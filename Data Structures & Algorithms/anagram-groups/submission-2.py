class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}

        for i in strs:
            k = "".join(sorted(i))
            if k not in grouped:
                grouped[k] = []
            grouped[k].append(i)
        return list(grouped.values())

