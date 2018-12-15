def bubble_sort(arr):
    not_sorted = True
    while(not_sorted):
        not_sorted = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                not_sorted = True
    return arr

def main():
    print(bubble_sort([1, 3, 5, 2, 8, 0, -1, -4]))

if __name__ == '__main__':
    main()
