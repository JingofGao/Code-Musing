"""
面试题 02.07. 链表相交

给你两个单链表的头节点 headA 和 headB ，
请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = self.getLen(headA)
        lenB = self.getLen(headB)

        curA = headA
        curB = headB
        if lenA-lenB >= 0:
            for _ in range(lenA-lenB):
                curA = curA.next
        else:
            for _ in range(lenB-lenA):
                curB = curB.next

        while curA!=None:
            if curA==curB:
                break
            else:
                curA = curA.next
                curB = curB.next
        return curA

    def getLen(self, head):
        link_len = 0
        while head != None:
            head = head.next
            link_len += 1
        return link_len


if __name__ == '__main__':
    # 无测试用例
    a = 1