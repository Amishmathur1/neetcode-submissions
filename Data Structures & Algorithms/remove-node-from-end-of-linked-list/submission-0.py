# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        count = 0
        temp = head
        while temp:
            temp = temp.next
            count += 1
        
        value = count - n
        temp1 = head 
        count = 0
        prev = None
        if value == 0:
            return head.next

        while count < value and temp1.next:
            prev = temp1
            temp1 = temp1.next 
            count += 1

        prev.next = temp1.next
        return head