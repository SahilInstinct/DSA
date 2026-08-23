class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1

        for ch in s:

            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '+':
                result += sign * num
                num = 0
                sign = 1

            elif ch == '-':
                result += sign * num
                num = 0
                sign = -1

            elif ch == '(':
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1

            elif ch == ')':
                result += sign * num
                num = 0

                sign = stack.pop()
                previous_result = stack.pop()

                result = previous_result + sign * result

        result += sign * num

        return result