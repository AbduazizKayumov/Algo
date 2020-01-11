def counting_sort(arr):
    count = [0] * 10
    for i in range(len(arr)):
        count[arr[i]] += 1

    answer = []
    for i in range(len(count)):
        answer.extend([i] * count[i])

    return answer


res = counting_sort([4, 1, 2, 6, 5, 8, 0, 7, 3, 9])
print(res)
