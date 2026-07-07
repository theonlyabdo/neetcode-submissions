class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputs = {}
        for str in strs:
            key = tuple(sorted(str))
            if key not in outputs:
                outputs[key] = []
            outputs[key].append(str)
        
        return list(outputs.values())