class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = dict()
        used = set()
        for i in range(len(s)):
            if s[i] not in mapping and t[i] not in used:
                mapping[s[i]] = t[i]
                used.add(t[i])
            elif s[i] not in mapping and t[i] in used:
                return False
            else:
                if t[i] != mapping[s[i]]:
                    return False
        return True
        