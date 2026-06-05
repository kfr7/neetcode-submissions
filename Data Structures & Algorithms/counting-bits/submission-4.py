class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            cleaned = bin(i)[2:]
            count = 0
            for j in range(len(cleaned)):
                if cleaned[j] == '1':
                    count += 1

            result.append(count)
        return result
        