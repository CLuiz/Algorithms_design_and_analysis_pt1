"""Python implementation of the merge sort algorithm"""

def merge(left, right):
    """ List merge helper function for merge_sort."""
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            del left[0]
        else:
            result.append(right[0])
            del right[0]
    if not left:
        result.extend(right)
    else:
        result.extend(left)
    return result


def merge_sort(lst):
    """Implementation of the merge sort algorithm."""
    if len(lst) < 2:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)
