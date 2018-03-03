def binarySearch(target, sortedList):
    left = 0
    right = len(sortedList) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if target == sortedList[midpoint]:
            return midpoint
        elif target > sortedList[midpoint]:
            left = midpoint + 1
        else:
            right = midpoint - 1
        return -1


b = [1, 2, 5, 6, 9]

print(binarySearch(4, b))
