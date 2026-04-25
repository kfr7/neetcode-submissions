class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                second_number = numbers.pop()
                first_number = numbers.pop()
                if token == "+":
                    numbers.append(first_number+second_number)
                elif token == "-":
                    numbers.append(first_number-second_number)
                elif token == "*":
                    numbers.append(first_number*second_number)
                else:
                    numbers.append(int(first_number/second_number))
            else:
                numbers.append(int(token))
        return numbers.pop()
        