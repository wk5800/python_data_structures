def search(target, a):
    for i in range(len(a)):
        if target == a[i]:
            return i
    return -1
b = [5, 6, 2, 1, 3]
target = 6

print(search(target=target,a=b))