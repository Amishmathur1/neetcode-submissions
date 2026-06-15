# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        num2 = ''

        temp1 = l1
        while temp1:
            num1 += str(temp1.val)
            temp1 = temp1.next
        
        temp2 = l2
        while temp2:
            num2 += str(temp2.val)
            temp2 = temp2.next
        
        print(num1, num2)
        x = int(num1[::-1]) + int(num2[::-1])
        x = str(x)
        l = [i for i in x[::-1]]
        x = ListNode(0)
        temp = x
        for i in l:
            new_node = ListNode(int(i))
            temp.next = new_node
            temp = temp.next
        return x.next
