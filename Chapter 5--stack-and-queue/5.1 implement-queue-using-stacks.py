"""
232. 用栈实现队列

请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作
"""


### 用双栈实现一个队列
# 入队，放入栈1就行
# 出队，如果栈2中有元素，出栈2；否则先将栈1中的所有元素压入栈2，再出栈2

class MyQueue(object):

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack_2)>0:
            return self.stack_2.pop()
        else:
            while len(self.stack_1)>0:
                self.stack_2.append(self.stack_1.pop())
            return self.stack_2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if len(self.stack_2)>0:
            return self.stack_2[-1]
        else:
            while len(self.stack_1)>0:
                self.stack_2.append(self.stack_1.pop())
            return self.stack_2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack_1)==0 and len(self.stack_2)==0


if __name__ == '__main__':
    myQueue = MyQueue()
    print(myQueue.push(1))  # queue is: [1]
    print(myQueue.push(2))  # queue is: [1, 2]
    print(myQueue.peek())  # return 1
    print(myQueue.pop())  # return 1, queue is [2]
    print(myQueue.empty())  # return false
