"""
142. 环形链表 II

给定一个链表的头节点  head ，返回链表开始入环的第一个节点。
如果链表无环，则返回 null。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = None
        fast = head
        slow = head
        while fast != None and fast.next !=None:
            fast = fast.next.next
            slow = slow.next

            # 有环
            if fast==slow:
                ind0 = head
                ind1 = fast
                while ind0!=ind1:
                    ind0 = ind0.next
                    ind1 = ind1.next
                ans = ind0
                break
        return ans


if __name__ == '__main__':
    # 无测试用例
    a = 1