"""
19. 删除链表的倒数第 N 个结点

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode()
        dummyHead.next = head
        pre = dummyHead
        cur = dummyHead
        for _ in range(n):
            cur = cur.next
        while cur.next != None:
            pre = pre.next
            cur = cur.next
        pre.next = pre.next.next
        return dummyHead.next


if __name__ == '__main__':
    # 无测试用例
    a = 1