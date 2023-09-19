"""
150. 逆波兰表达式求值

给你一个字符串数组 tokens ，表示一个根据 逆波兰表示法 表示的算术表达式。
请你计算该表达式。返回一个表示表达式值的整数。

注意：
有效的算符为 '+'、'-'、'*' 和 '/' 。
每个操作数（运算对象）都可以是一个整数或者另一个表达式。
两个整数之间的除法总是 向零截断 。
表达式中不含除零运算。
输入是一个根据逆波兰表示法表示的算术表达式。
答案及所有中间计算结果可以用 32 位 整数表示。
"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for ele in tokens:
            if ele in ['+','-','*','/']:
                b = stack.pop()
                a = stack.pop()
                if ele == '+':
                    stack.append(a+b)
                elif ele == '-':
                    stack.append(a-b)
                elif ele == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(float(a)/b))  # 两个整数之间的除法向零截断
            else:
                stack.append(int(ele))
        return stack.pop()


if __name__ == '__main__':
    tokens = ["2","1","+","3","*"]
    solu = Solution()
    print(solu.evalRPN(tokens))  # 9
