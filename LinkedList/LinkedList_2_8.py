from typing import Optional

from LinkedListDataModel import ListNode

def getLoopNode(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    
    nodesVisited = set()
    while head:
        if head in nodesVisited:
            return head
        nodesVisited.add(head)
        head = head.next
    return None