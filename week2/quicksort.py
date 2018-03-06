""" Python implementation of the quicksort algorithm """

#def partition(arr, start, end):
#    pivot = start
#    for i in range(start + 1, end + 1):
#        if arr[i] <= arr[start]:
#            pivot += 1
#            arr[i], arr[pivot] = arr[pivot], arr[i]
#    arr[pivot], arr[start] = arr[start], arr[pivot]
#    return pivot
#
#def quicksort(arr, start=0, end=None):
#    if end is None:
#        end = len(arr) - 1
#
#    def _quicksort(arr, start, end):
#        if start >= end:
#            return
#        pivot = partition(arr, start, end)
#        _quicksort(arr, start, pivot - 1)
#        _quicksort(arr, pivot + 1, end)
#    return _quicksort(arr, start, end)
#
def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot



def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)
