# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = head = ListNode('dummy')
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                list2 = list2.next
            current = current.next
        if list1 is None and list2 is None:
            return head.next
        if list1 is None:
            current.next = list2
        else:
            current.next = list1
        return head.next
