def diagonalDifference(arr):
    a=0
    b=0
    for i in range(len(arr)):
         a=a+arr[i][i]
         b=b+arr[i][len(arr)-i-1]
    return abs(a-b)