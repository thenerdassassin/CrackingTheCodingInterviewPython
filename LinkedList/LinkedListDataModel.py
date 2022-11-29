from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def printList(self):
        currentNode = self
        toPrint = "["
        while currentNode:
            toPrint += (str(currentNode.val) + ",")
            currentNode = currentNode.next
        toPrint += "]"
        print(toPrint)

def createListFromArray(values: List[int]) -> ListNode:
    if not values or len(values) == 0:
        return None
    head = ListNode(values[0])
    currentNode = head
    for i in range(1, len(values)):
        currentNode.next = ListNode(values[i])
        currentNode = currentNode.next
    return head