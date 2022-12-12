# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        pass

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.recursive_add(l1, l2, 0)

    def recursive_add(self, l1: ListNode, l2: ListNode, carry_one: bool) -> ListNode:

        my_sum = l1.val + l2.val + carry_one
        if my_sum >= 10:
            my_sum -= 10
            exceeds_ten = 1
        else:
            exceeds_ten = 0

        answer_node = ListNode(val=my_sum)

        if l1.next and l2.next:
            answer_node.next = self.recursive_add(l1.next, l2.next, exceeds_ten)
        elif l1.next:
            if exceeds_ten:
                # dummy_node = ListNode()
                answer_node.next = self.recursive_add(l1.next, ListNode(), exceeds_ten)
            else:
                answer_node.next = l1.next
        elif l2.next:
            if exceeds_ten:
                # dummy_node = ListNode()
                answer_node.next = self.recursive_add(ListNode(), l2.next, exceeds_ten)
            else:
                answer_node.next = l2.next
        elif exceeds_ten:
            answer_node.next = ListNode(1)

        return answer_node


def create_link(my_list):
    root = ListNode(val=my_list[0])
    prev_node = root
    for num in my_list[1:]:
        this_node = ListNode(val=num)
        prev_node.next = this_node
        prev_node = this_node
    return root


num_1 = create_link([2, 4, 6])
num_2 = create_link([5, 4, 4])

dummy = Solution()
answer = dummy.addTwoNumbers(num_1, num_2)

print("Hello World!")
