def indexofMin(a):
    """
    找到list中的最小值
    :param a:
    :return:
    """

    startindex = 0
    nextindex = 1

    while nextindex < len(a):
        if a[startindex] > a[nextindex]:
            startindex = nextindex
        nextindex += 1
    return a[startindex]


b = [5, 6, 2, 1, 3]

minvalue = indexofMin(b)
print(minvalue)
