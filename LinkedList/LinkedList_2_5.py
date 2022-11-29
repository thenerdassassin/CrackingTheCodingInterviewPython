from LinkedListDataModel import ListNode, createListFromArray

def sumLists(first: ListNode, second: ListNode) -> int:
    answer = 0
    index = 1
    while first or second:
        firstNumber = 0
        secondNumber = 0
        if first:
            firstNumber = first.val * index
            first = first.next
        if second:
            secondNumber = second.val * index
            second = second.next
        answer += (firstNumber + secondNumber)
        index = index * 10
    return answer

def sumListsForwardOrder(first: ListNode, second: ListNode) -> int:
    firstNumber = ""
    secondNumber = ""

    while first or second:
        if first:
            firstNumber += str(first.val)
            first = first.next
        if second:
            secondNumber += str(second.val)
            second = second.next
    
    if not firstNumber:
        return int(secondNumber)
    if not secondNumber:
        return int(firstNumber)
    return int(firstNumber) + int(secondNumber)


firstList = createListFromArray([1,2,3])
secondList = createListFromArray([5,2,4])
sum = sumLists(firstList, secondList)
assert(sum == 746)
assert(sumListsForwardOrder(firstList, secondList) == 647)

thirdList = createListFromArray([9,9,7])
fourthList = createListFromArray([5,2,4])
sum = sumLists(thirdList, fourthList)
assert(sum == 1224)
assert(sumListsForwardOrder(thirdList, fourthList) == 1521)

sum = sumLists(thirdList, None)
assert(sum == 799)
assert(sumListsForwardOrder(thirdList, None) == 997)

fifthList = createListFromArray([0,0,0,9,9,9])
sum = sumLists(thirdList, fifthList)
assert(sum == 999799)
assert(sumListsForwardOrder(thirdList, fifthList) == 1996)

print("Success!")