def quick_sort(array, left, right):
    if right <= left:
        return
    low = left
    high = right
    mid = array[low]
    while low < high:
        while low < high and array[high] > mid:
            high -= 1
        array[low] = array[high]
        while low < high and array[low] < mid:
            low += 1
        array[high] = array[low]
    array[low] = mid
    quick_sort(array, left, low - 1)
    quick_sort(array, low + 1, right)

if __name__ == '__main__':
    array = [9, 8, 7, 6, 5, 4, 2, 1]
    quick_sort(array, 0, len(array) - 1)
    print array




