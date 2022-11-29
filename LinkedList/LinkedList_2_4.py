
from typing import Optional
from LinkedListDataModel import ListNode, createListFromArray


def partitionList(head: Optional[ListNode], p: int) -> ListNode:
    partitionedHead = None
    greaterHead = None #Greater or Equal

    currentLess = None
    currentGreater = None

    currentNode = head
    while currentNode:
        if currentNode.val < p:
            if not currentLess:
                currentLess = currentNode
                partitionedHead = currentLess
                currentNode = currentNode.next
                currentLess.next = None
            else:
                currentLess.next = currentNode
                currentNode = currentNode.next
                currentLess = currentLess.next
                currentLess.next = None
        else:
            if not currentGreater:
                currentGreater = currentNode
                greaterHead = currentGreater
                currentNode = currentNode.next
                currentGreater.next = None
            else:
                currentGreater.next = currentNode
                currentNode = currentNode.next
                currentGreater = currentGreater.next
                currentGreater.next = None
    
    if not partitionedHead:
        return greaterHead

    currentLess.next = greaterHead
    return partitionedHead

 
firstList = createListFromArray([3,5,8,5,10,2,1])
partitionList(firstList, 2).printList()   