
import string
from typing import List

class BinaryNode:
    def __init__(self, value: int, left, right):
        self.value = value
        self.left = left
        self.right = right

class Node:
    def __init__(self, name: string, children):
        self.name = name
        self.children = children
        self.visited = False

class Graph:
    def __init__(self, nodes: List[Node]):
        self.nodes  = nodes