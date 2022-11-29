
from LinkedList.LinkedListDataModel import ListNode

def deleteMiddleNode(nodeToDelete: ListNode):
    if not nodeToDelete:
        return
        
    assert(nodeToDelete.next, "Can not delete the Final Node of singly linked list")

    nextNode = nodeToDelete.next

    nodeToDelete.val = nextNode.val
    nodeToDelete.next = nextNode.next
    
