"""
24. 两两交换链表中的节点

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode()
        dummyHead.next = head
        pre = dummyHead
        while pre.next != None and pre.next.next != None:
            node_0 = pre.next
            node_1 = pre.next.next
            pre.next = node_1
            node_0.next = node_1.next
            node_1.next = node_0
            pre = node_0
        return dummyHead.next


if __name__ == '__main__':
    # 无测试用例
    a = 1