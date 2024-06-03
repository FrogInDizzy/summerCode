from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
        
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10

            current.next = ListNode(new_val)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next
    

def create_linked_list(numbers):
    dummy = ListNode()
    current = dummy
    for number in numbers:
        current.next = ListNode(number)
        current = current.next
    return dummy.next

def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

if __name__ == "__main__":
    # Create test cases
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])

    # Add the two numbers
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    # Print the result
    print_linked_list(result)  # Expected output: 7 -> 0 -> 8 -> None