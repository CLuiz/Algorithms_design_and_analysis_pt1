"""Merge sort implementation that also counts inversions """

def merge_sort_and_count(lst, cnt):
    if len(lst) < 2:
        return lst

    mid = len(lst) // 2
    return merge_and_count(
        merge_sort_and_count(lst[:mid], cnt),
        merge_sort_and_count(lst[mid:], cnt), cnt)

def merge_and_count(left, right, cnt):
    result = []
    while left and right:
        s = left if left[0] < right[0] else right
        result.append(s.pop(0))

        if (s == right):
            cnt[0] += (len(left))
        rest = left if left else right
    result.extend(rest)
    return result

#correct: 2407905288
