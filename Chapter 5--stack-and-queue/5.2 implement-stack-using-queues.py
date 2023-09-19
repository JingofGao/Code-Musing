"""
225. 用队列实现栈

请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作
"""


### 用一个队列实现栈
# 入栈，入队
# 出栈，先将前n-1个元素先出队再入队，再执行出队操作

from collections import deque

class MyStack(object):
    def __init__(self):
        self.q = deque()


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)


    def pop(self):
        """
        :rtype: int
        """
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        return self.q.popleft()


    def top(self):
        """
        :rtype: int
        """
        return self.q[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return not self.q


if __name__ == '__main__':
    myStack = MyStack()
    print(myStack.push(1))
    print(myStack.push(2))
    print(myStack.top())  # 返回 2
    print(myStack.pop())  # 返回 2
    print(myStack.empty())  # 返回 False
