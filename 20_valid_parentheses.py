class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        for bracket in s:
            if bracket in ("(", "[", "{"):
                brackets.append(bracket)
                continue
            
            if len(brackets) == 0:
                return False

            last_bracket = brackets[-1]
            if last_bracket == "(" and bracket == ")":
                brackets.pop()
            elif last_bracket == "[" and bracket == "]":
                brackets.pop()
            elif last_bracket == "{" and bracket == "}":
                brackets.pop()
            else:
                return False

        if len(brackets) != 0:
            return False
            
        return True
            