class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {char : index for index,char in enumerate(s)}
        stack, seen = [], set()

        for i in range(len(s)):
            if s[i] in seen:
                continue
            else:
                while stack and stack[-1] > s[i] and last[stack[-1]] > i:
                    el = stack.pop()
                    seen.remove(el)
            stack.append(s[i])
            seen.add(s[i])

        return "".join(stack)
        