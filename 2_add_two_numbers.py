# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)

        last = result

        next_value = 0
        while l1 or l2 or next_value:
            actual_value = next_value

            if l1:
                actual_value += l1.val
                l1 = l1.next
                
            if l2:
                actual_value += l2.val
                l2 = l2.next
            
            next_value = actual_value // 10
            actual_value = actual_value % 10

            last.next = ListNode(actual_value)
            last = last.next

        return result.next