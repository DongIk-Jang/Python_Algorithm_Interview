# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        result = []
        if not head:
            return True
        
        node = head
        while node:
            result.append(node.val)
            node = node.next
        
        if result == result[::-1]:
            return True
        else:
            return False

'''
Runner를 이용한 풀이도 가능하다.
전체적인 풀이 방법과 과정은 이해했으나
다중할당에 대한 부분은 아직 제대로 이하지 못한 것 같다.
'''

def isPalindrome(self, head):
    rev = None
    slow = fast = head
    # 러너를 이용해 역순 연결리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    
    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev