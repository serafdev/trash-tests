def binary_search(arr, val):
    if len(arr) == 0 or (len(arr) == 1 and not arr[0] == val):
        return False

    mid = arr[len(arr) / 2]

    print(mid)
    print(arr)
    
    if val == mid: return True
    if val < mid: return binary_search(arr[:len(arr)/2], val)
    if val > mid: return binary_search(arr[len(arr)/2:], val)



def main():
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 5))

if __name__ == '__main__':
    main()
