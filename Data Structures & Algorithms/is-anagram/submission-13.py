class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt1, cnt2 = Counter(s), Counter(t)
        return cnt2 == cnt1