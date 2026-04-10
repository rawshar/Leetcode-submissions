# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
prev=None
    curr  t2
None <-0 1->
prev=curr
curr=t2
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        while head:
            temp=head.next
            head.next=prev
            prev=head
            head=temp
        return prev
        