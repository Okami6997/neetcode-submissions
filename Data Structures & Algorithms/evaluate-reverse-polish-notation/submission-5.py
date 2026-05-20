class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for c in tokens:
            match c:
                case "+":
                    s.append(int(s.pop()) + int(s.pop()))
                case "-":
                    a, b = int(s.pop()), int(s.pop())
                    s.append(int(b - a))
                case "*":
                    s.append(int(s.pop()) * int(s.pop()))
                case "/":
                    a, b = int(s.pop()), int(s.pop())
                    s.append(int(float(b)/ a))
                case _:
                    s.append(int(c))
        return s[0]
