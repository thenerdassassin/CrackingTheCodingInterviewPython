from collections import deque

from TreesAndGraphs.TreesAndGraphsDataModel import Node

def isRoute(one: Node, two: Node) -> bool:
    if one == two:
        return True
    queue = deque()
    queue.append(one)
    one.visited = True

    while queue.count() > 0:
        current = queue.popleft()
        if not current:
            continue
        current.visited = True
        for n in current.nodes:
            if n == two:
                return True
            if not n.visited:
                n.visited = True
                queue.append(two)
    return False