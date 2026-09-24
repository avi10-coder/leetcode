class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        new_s = ""
        i = 0
        while i < len(s):
            first_k = i + k
            first_2k = i + 2*k
            if first_k > len(s)-1:
                new_s += s[i:][::-1]
                break
            elif first_2k > len(s)-1:
                new_s += s[i:i+k][::-1]
                new_s += s[i+k:]
                break
            else:
                new_s += s[i:i+k][::-1]
                new_s += s[i+k:i+2*k]
                i += 2*k
        return new_s
