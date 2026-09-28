class Solution:

    def __init__(self):
        self.out = []

    def dfs(self, s, index, result):
        if index == len(s):
            self.out.append(result)
            return
        else:
            for i in range(index, len(s)):
                if s[index:i+1] == s[index:i+1][::-1]:
                    self.dfs(s, i+1, result + [s[index:i+1]])
        
    def partition(self, s: str) -> list[list[str]]:
        self.dfs(s, 0, [])
        return self.out
        