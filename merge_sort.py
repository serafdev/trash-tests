def merge(a, b):
    arr = []

    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            arr.append(b[0])
            del b[0]
        else:
            arr.append(a[0])
            del a[0]

    if a:
        arr = arr + a
    elif b:
        arr = arr + b

    return arr


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    arr1 = arr[:len(arr)//2]
    arr2 = arr[len(arr)//2:]

    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)

    print(arr1)
    print(arr2)
    return merge(arr1, arr2)


def main():
    arr = merge_sort([1, 2, 5, 6, 7, 3, 4])
    print(arr)


if __name__ == '__main__':
    main()

# e.g
# Arr: 9, 3, 8, 1, 5, 6, 4, 2
# Arr1: 9, 3, 8, 1
# Arr2: 5, 6, 4, 2

# Arr1.1: 9, 3
# Arr1.2: 8, 1

# Arr2.1: 5, 6
# Arr2.2: 4, 2

# [9], [3], [8], [1], [5], [6], [4], [2]

# [3, 9], [1, 8], [5, 6], [2, 4]

# [1, 3, 8, 9], [2, 4, 5, 6]

# [1, 2, 3, 4, 5, 6, 8, 9]
