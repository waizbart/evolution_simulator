def insertion_sort(arr, key=lambda x: x.size):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and key(arr[j]) > key(current):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current