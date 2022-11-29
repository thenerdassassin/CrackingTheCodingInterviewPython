from typing import List
from TreesAndGraphs.TreesAndGraphsDataModel import BinaryNode


def buildBinarySearchTree(elements: List[int]) -> BinaryNode:
    if len(elements) == 0:
        return None
    if len(elements) == 1:
        return BinaryNode(elements[0], None, None)


    midpoint = round(len(elements) / 2) # Root of tree

    leftNode = buildBinarySearchTree(elements[0:midpoint-1])
    rightNode = buildBinarySearchTree(elements[midpoint+1:-1])
    return BinaryNode(elements[midpoint], leftNode, rightNode)
