# Find a peak from 1D array
# Any element is a pick if it is bigger than its adjacent elements: left <= middle <= right
# 1) Pick a middle element
# 2) If the middle element is less than the right element,
# try to find a peak from the right half of the array
# 3) If the middle element is less than the left element,
# try to find a peak from the left half of the array
# 4) else the middle element is a peak
def peak_finder(arr):
    l = -1
    r = len(arr)
    peak = arr[0]
    while r - l > 1:
        mid = (r + l) >> 1
        if mid == 0 or mid == len(arr) - 1:
            peak = arr[mid]
            break
        if arr[mid] < arr[mid - 1]:
            r = mid
        elif arr[mid] < arr[mid + 1]:
            l = mid
        else:
            peak = arr[mid]
            break
    return peak


# Find a peak from 2D array
# 1) Pick a middle column: j = m/2
# 2) Find global maximum on column j at (i, j)
# 3) Compare (i, j - 1), (i, j) , (i, j + 1)
# 4) Pick left columns if (i, j - 1) > (i, j)
# 5) Similar for right
# 6) (i, j) if (i, j - 1)<=(i, j)<=(i, j + 1)
def peak_finder_2D(arr):
    l = -1
    r = len(arr[0])
    peak = 0
    while r - l > 1:
        mid = (r + l) >> 1
        global_max = 0
        for i in range(len(arr)):
            if arr[i][mid] > arr[global_max][mid]:
                global_max = i

        if mid == 0 or mid == len(arr[global_max]) - 1:
            peak = arr[global_max][mid]
            break

        if arr[global_max][mid] < arr[global_max][mid - 1]:
            r = mid
        elif arr[global_max][mid] < arr[global_max][mid + 1]:
            l = mid
        else:
            peak = arr[global_max][mid]
            break
    return peak


res = peak_finder_2D([[10, 8, 10, 10],
                      [14, 13, 12, 11],
                      [15, 9, 11, 21],
                      [16, 17, 19, 20]])
print(res)
