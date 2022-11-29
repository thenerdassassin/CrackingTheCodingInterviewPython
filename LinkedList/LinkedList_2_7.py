from typing import Optional

from LinkedListDataModel import ListNode

def getIntersection(aList: Optional[ListNode], bList: Optional[ListNode]) -> Optional[ListNode] ->
    if not aList or not bList:
        return None
    
    nodesVisited = set()
    while aList or bList:
        if aList:
            if aList in nodesVisited:
                return aList
            nodesVisited.add(aList)
            aList = aList.next
        if bList:
            if bList in nodesVisited:
                return bList
            nodesVisited.add(bList)
            bList = bList.next
    return None