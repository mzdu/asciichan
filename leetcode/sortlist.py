"""
Sort a linked list in O(n log n) time using constant space complexity
"""
#wrong.....

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        
        if head:
            p1 = head
            nodeList = []
            #traverseList
            while p1 != None:
                nodeList.append(p1.val)
                p1 = p1.next
                
            nodeList.sort()
            
            print nodeList
            
            origlen = len(nodeList)
            prev = None
            while nodeList:
                value = nodeList.pop()
                p = ListNode(value)
                 
                if len(nodeList) == (origlen-1):
                    p.next = None
                    prev = p
                     
                else:
                    p.next = prev
                    prev = p
                    
                print 'p.value:', p.val,'p.next:',p.next, 'prev:', prev
            return prev
        else:
            return head
        
        
a1 = ListNode(2)
a2= ListNode(1)
b1 = ListNode(9)
b2 = ListNode(8)
b3 = ListNode(7)
b4 = ListNode(11)

a1.next = a2
a2.next = b1
b1.next = b2
b2.next = b3
b3.next = b4
b4.next = None

sol = Solution()
print sol.sortList(a1)


