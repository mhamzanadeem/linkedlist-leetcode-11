# LeetCode Linked List — 11 Problems

Repo: https://github.com/mhamzanadeem/linkedlist-leetcode-11

## Solutions

| # | Problem | File |
|---|---------|------|
| 1 | Reverse Linked List | [reverse_linked_list.py](reverse_linked_list.py) |
| 2 | Merge Two Sorted Lists | [merge_two_sorted_lists.py](merge_two_sorted_lists.py) |
| 3 | Middle of the Linked List | [middle_of_the_linked_list.py](middle_of_the_linked_list.py) |
| 4 | Linked List Cycle | [linked_list_cycle.py](linked_list_cycle.py) |
| 5 | Palindrome Linked List | [palindrome_linked_list.py](palindrome_linked_list.py) |
| 6 | Remove Duplicates from Sorted List | [remove_duplicates_from_sorted_list.py](remove_duplicates_from_sorted_list.py) |
| 7 | Intersection of Two Linked Lists | [intersection_of_two_linked_lists.py](intersection_of_two_linked_lists.py) |
| 8 | Delete Node in a Linked List | [delete_node_in_a_linked_list.py](delete_node_in_a_linked_list.py) |
| 9 | Delete Nodes From Linked List Present in Array | [delete_nodes_from_linked_list_present_in_array.py](delete_nodes_from_linked_list_present_in_array.py) |
| 10 | Design Browser History | [design_browser_history.py](design_browser_history.py) |
| 11 | Design HashMap | [design_hashmap.py](design_hashmap.py) |

---

## Skill Check 1 — Iterative Reverse Linked List (from memory)

```python
class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_tmp = current.next   # 1. save next
            current.next = prev       # 2. reverse the arrow
            prev = current            # 3. advance prev
            current = next_tmp        # 4. advance current
        return prev                  # new head
```

### Pointer diagram — Reverse Linked List

```
START
prev  -> None
curr  -> [1] -> [2] -> [3] -> [4] -> None

--- iter 1 ---
next_tmp = [2]
[1].next = None        (was [2])
prev = [1]
curr = [2]
state:  [1] -> None      [2] -> [3] -> [4] -> None

--- iter 2 ---
next_tmp = [3]
[2].next = [1]
prev = [2]
curr = [3]
state:  [2] -> [1] -> None      [3] -> [4] -> None

--- iter 3 ---
next_tmp = [4]
[3].next = [2]
prev = [3]
curr = [4]
state:  [3] -> [2] -> [1] -> None      [4] -> None

--- iter 4 ---
next_tmp = None
[4].next = [3]
prev = [4]
curr = None
DONE -> return prev = [4] -> [3] -> [2] -> [1] -> None
```

---

## Skill Check 2 — Merge Two Sorted Lists + dummy node

```python
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)   # placeholder so we never special-case the head
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2   # attach the leftover tail
        return dummy.next
```

### Pointer diagram — Merge Two Sorted Lists

```
list1:  [1] -> [3] -> [5] -> None
list2:  [2] -> [4] -> [6] -> None

dummy -> (0)
cur = dummy

cmp 1 vs 2  -> take 1 :  dummy -> [1]   cur=[1]   list1=[3]->[5]
cmp 3 vs 2  -> take 2 :  [1] -> [2]     cur=[2]   list2=[4]->[6]
cmp 3 vs 4  -> take 3 :  [2] -> [3]     cur=[3]   list1=[5]
cmp 5 vs 4  -> take 4 :  [3] -> [4]     cur=[4]   list2=[6]
cmp 5 vs 6  -> take 5 :  [4] -> [5]     cur=[5]   list1=None
list1 empty -> attach list2:  [5] -> [6] -> None

RESULT (dummy.next):  [1] -> [2] -> [3] -> [4] -> [5] -> [6] -> None
```

### The dummy node trick — why it exists

Without a dummy, you must handle "where does the first merged node go?" as a
special case: check if `list1` or `list2` is null up front, pick the smaller as
the `head`, and only then start the loop. Two edge cases to get wrong:
1. One input list is empty -> return the other directly.
2. The very first comparison must assign to `head`, not to `prev.next`.

The dummy node is a throwaway sentinel. You always append through `current.next`
and return `dummy.next`, so the first node is treated exactly like every other
node. **The dummy saves you from the empty-input and "which list is the head"
edge cases** — the loop body never changes whether it's the first or last node.

---

## Skill Check 3 — Node diagrams drawn before coding (3 problems)

### A) Intersection of Two Linked Lists

```
A:  [4] -> [1] -> [8] -> [4] -> [5]
                    ^
B:  [5] -> [6] -> [1] -> [8] -> [4] -> [5]
                    ^
Two pointers: pA starts at A, pB at B.
When pA hits end, jump to B; when pB hits end, jump to A.
They meet at [8] after traversing the same total length.
```

### B) Remove Duplicates from Sorted List

```
[1] -> [1] -> [2] -> [3] -> [3] -> None
 cur^
if cur.val == cur.next.val: cur.next = cur.next.next  (skip dup)
else: cur = cur.next
=> [1] -> [2] -> [3] -> None
```

### C) Linked List Cycle (Floyd)

```
[3] -> [2] -> [0] -> [-4] --
        ^                  |
        |__________________|
slow (1 step), fast (2 steps). They meet inside the cycle;
reset one pointer to head, move both 1 step -> they meet at the cycle start.
```
