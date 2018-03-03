def swap(a, i, j):
    '''
    交换列表两元素位置
    :param a:
    :param i:
    :param j:
    :return:
    '''
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def selectionSort(a):
    i = 0
    while i < len(a) - 1:
        minIndex = i
        j = i + 1
        while j < len(a):
            if a[j] < a[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            swap(a, minIndex, j)
        i += 1

b = [1, 2, 5, 6, 9]
selectionSort(b)