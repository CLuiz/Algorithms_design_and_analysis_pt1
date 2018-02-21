""" Python implementation of the quicksort algorithm """

def partition(arr, start, end, cnt):
    pivot = start
    for i in range(start + 1, end + 1):
        cnt += 1
        if arr[i] <= arr[start]:
            pivot += 1
            arr[i], arr[pivot] = arr[pivot], arr[i]
    arr[pivot], arr[start] = arr[start], arr[pivot]
    print(pivot)
    return pivot

def quicksort(arr, start=0, end=None, cnt=0):
    if end is None:
        end = len(arr) - 1

        def _quicksort(arr, start, end):
            if start >= end:
                return
            pivot = partition(arr, start, end, cnt)
            _quicksort(arr, start, pivot - 1)
            _quicksort(arr, pivot + 1, end)
        return _quicksort(arr, start, end), cnt

