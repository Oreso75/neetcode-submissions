class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for parenthesis in s:
            if parenthesis in "({[":
                stack.append(parenthesis)

            elif parenthesis == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()

            elif parenthesis == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()

            elif parenthesis == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()

        return stack == []
        
            
        