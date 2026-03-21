def miniMaxSum(arr):
    sum = 0
    for i in arr:
        sum += i

    min = arr[0]
    max = arr[0]

    for j in arr:
        if j < min:
            min = j
        if j > max:
            max = j

    print(sum - max, sum - min)


# İkinci çözüm:

def miniMaxSum2(arr):
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])

    print(min_sum, max_sum)