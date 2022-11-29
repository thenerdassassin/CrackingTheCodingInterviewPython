from typing import Optional

from LinkedList.LinkedListDataModel import ListNode, createListFromArray
        
def removeDups(head: Optional[ListNode]) -> ListNode:
    if not head:
        return head

    visitedNodes = set()

    currentNode = head
    while currentNode:
        visitedNodes.add(currentNode.val)
        if isNextNodeDuplicate(currentNode.next, visitedNodes):
            currentNode.next = currentNode.next.next
        else:
            currentNode = currentNode.next
    return head

def isNextNodeDuplicate(node: ListNode, visistedNodes: set) -> bool:
    if not node:
        return False
    
    return node.val in visistedNodes


firstList = createListFromArray([4,5,6])
removeDups(firstList).printList()

secondList = createListFromArray([4,5,6,4])
removeDups(secondList).printList()

thirdList = createListFromArray([4,4,4,4])
removeDups(thirdList).printList()
