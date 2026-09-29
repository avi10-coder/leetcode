class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = [string for string in path.split("/") if string]
        stack = []
        for string in path_list:
            if string == ".." and stack:
                stack.pop()
            elif (string == ".") or (string == ".." and not stack):
                continue
            else:
                stack.append(string) 
        return "/"+"/".join(stack)