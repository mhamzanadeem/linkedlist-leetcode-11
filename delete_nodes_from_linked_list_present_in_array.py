class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        nums = set(nums)

        dummy = ListNode(0)
        dummy.next = head

        current = dummy

        while current.next:
            if current.next.val in nums:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next