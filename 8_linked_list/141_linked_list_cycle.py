# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = []
        node = head
        while node is not None:
            if node in temp:
                return True
            if node.val == None:
                return False
            
            temp.append(node)
            node = node.next
            
        # print(temp)
        return False

'''
temp를 리스트 대신 set()으로 하고
set의 길이가 더이상 늘어나지 않는다면 True 리턴하도록할 수 있다.
'''

class Solution:
    def hasCycle2(self, head: ListNode) -> bool:
        temp = set()
        node = head
        while node:
            prev_len = len(temp)
            temp.add(node)
            if len(temp) == prev_len:
                return True
            node = node.next
        return False