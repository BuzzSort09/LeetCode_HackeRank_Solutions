# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        one_digit_sum = 0
        carry = 0
        
        root = output = ListNode(0)
        
        # 0(N)
        while l1 or l2 or carry:
            l1_value = l2_Value = 0    
            if l1:
                l1_value = l1.val
                l1 = l1.next
            if l2:
                l2_Value = l2.val    
                l2 = l2.next

            one_digit_sum = l1_value + l2_Value + carry            
            carry = one_digit_sum // 10
            one_digit_value = one_digit_sum % 10
            output.next = ListNode(one_digit_value)
            output = output.next            
            
        return root.next