class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(open_remain, close_remain, build):
            if open_remain == 0 and close_remain == 0:
                res.append(build)
                return
            if open_remain > 0:
                build += '('
                open_remain -= 1
                helper(open_remain, close_remain, build)     
                build = build[:-1]
                open_remain += 1
            if close_remain > open_remain:
                build += ')'
                close_remain -= 1
                helper(open_remain, close_remain, build)   
                build = build[:-1]
                close_remain += 1
        helper(n, n, '')
        return res


        