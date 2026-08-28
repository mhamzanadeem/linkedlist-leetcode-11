# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head 
        slow  = head

        # slow will stop at middle of linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            tmp = slow.next # value of next node of slow
            slow.next=prev #None
            prev = slow
            slow = tmp


        # check palindrome
        left , right = head , prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True