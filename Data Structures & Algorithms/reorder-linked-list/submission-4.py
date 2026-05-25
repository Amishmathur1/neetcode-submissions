# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head is None or head.next is None:
            return

        # Count length
        temp = head
        count = 0

        while temp:
            count += 1
            temp = temp.next

        mid = count // 2

        # Move to middle
        prevMid = head

        for _ in range(mid - 1):
            prevMid = prevMid.next

        # Split list
        temp = prevMid.next
        prevMid.next = None

        # Reverse second half
        prev = None
        curr = temp

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Merge both halves
        tempA = head
        tempB = prev

        tempA = head
        tempB = prev

        while tempA and tempB:

            nextA = tempA.next
            nextB = tempB.next

            tempA.next = tempB

            if nextA is None:
                break

            tempB.next = nextA

            tempA = nextA
            tempB = nextB