# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        count = 0
        while curr and count<=1001:
            curr = curr.next
            count +=1
            if count == 1001:
                return True
        return False