class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', ']':'[','}':'{'}

        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
        return not stack   