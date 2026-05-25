# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        temp = head
        x = set()

        while temp.next:
            if temp.val not in x:
                x.add(temp.val)
                temp = temp.next
            else:
                return True
        return False