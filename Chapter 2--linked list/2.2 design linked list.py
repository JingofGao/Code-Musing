"""
707. 设计链表

实现 MyLinkedList 类：
- MyLinkedList() 初始化 MyLinkedList 对象。
- int get(int index) 获取链表中下标为 index 的节点的值。如果下标无效，则返回 -1 。
- void addAtHead(int val) 将一个值为 val 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。
- void addAtTail(int val) 将一个值为 val 的节点追加到链表中作为链表的最后一个元素。
- void addAtIndex(int index, int val) 将一个值为 val 的节点插入到链表中下标为 index 的节点之前。
如果 index 等于链表的长度，那么该节点会被追加到链表的末尾。如果 index 比长度更大，该节点将 不会插入 到链表中。
- void deleteAtIndex(int index) 如果下标有效，则删除链表中下标为 index 的节点。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """

        if index < 0 or index + 1 > self.size:
            return -1

        cur = self.dummy_head
        for i in range(index):
            cur = cur.next
        return cur.next.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = ListNode(val=val)
        newNode.next = self.dummy_head.next
        self.dummy_head.next = newNode
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = ListNode(val=val)
        cur = self.dummy_head
        while cur.next != None:
            cur = cur.next
        cur.next = newNode
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return None

        newNode = ListNode(val=val)
        cur = self.dummy_head
        for i in range(index):
            cur = cur.next
        newNode.next = cur.next
        cur.next = newNode
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return None

        cur = self.dummy_head
        for i in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1


if __name__ == '__main__':
    obj = MyLinkedList()
    obj.addAtHead(1)  # [1]
    obj.addAtTail(3)  # [1,3]
    obj.addAtIndex(1,2)  # [1, 2, 3]
    print(obj.get(1))  # 2
    obj.deleteAtIndex(1)  # [1, 3]
    print(obj.get(1))  # 3
