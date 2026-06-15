"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}

        temp = head

        while temp:
            old_to_new[temp] = Node(temp.val)
            temp = temp.next

        temp = head

        while temp:
            copy = old_to_new[temp]

            copy.next = old_to_new.get(temp.next)
            copy.random = old_to_new.get(temp.random)

            temp = temp.next
            
        return old_to_new.get(head)