
from typing import Optional

from LinkedListDataModel import ListNode, createListFromArray

def getKthToLast(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
        return None
    
    listSize = 0
    currentNode = head
    while currentNode:
        listSize += 1
        currentNode = currentNode.next
    
    if listSize < k:
        return None

    currentIndex = 0
    goalIndex = listSize - k
    currentNode = head
    while currentIndex < goalIndex:
        currentNode = currentNode.next
        currentIndex += 1
    return currentNode

firstList = createListFromArray([1,2,3])
firstAnswer = getKthToLast(firstList, 1)
firstAnswer.printList()
assert(firstAnswer.val == 3)

secondList = createListFromArray([1,2,3,4,5])
secondAnswer = getKthToLast(secondList, 4)
secondAnswer.printList()
assert(secondAnswer.val == 2)

thirdList = createListFromArray([1,2,3,4,5])
thirdAnswer = getKthToLast(thirdList, 7)
assert(thirdAnswer == None)

fourthList = createListFromArray([1,2,3,4,5])
fourthAnswer = getKthToLast(fourthList, 5)
fourthAnswer.printList()
assert(fourthAnswer.val == 1)

print("Success!")
