def compareTriplets(a, b):
    result_a=0
    result_b=0
    for i in range(len(a)):
        if a[i]>b[i]:
            result_a=result_a+1
        elif a[i]<b[i]:
            result_b=result_b+1
    return [result_a,result_b]