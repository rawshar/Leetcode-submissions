# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        NodeDummy=ListNode(0)
        head=NodeDummy
        while list1 and list2:
            if list1.val <=list2.val:
                NodeDummy.next=list1
                list1=list1.next
            else:
                NodeDummy.next=list2
                list2=list2.next
            NodeDummy=NodeDummy.next
        NodeDummy.next= list1 if list1 else list2
        return head.next
            
        