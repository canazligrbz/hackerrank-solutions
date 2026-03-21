def plusMinus(arr):
    pozitive_sum=0
    negative_sum=0
    zero=0
    n= len(arr)
    for i in range(len(arr)):
        if arr[i]>0:
            pozitive_sum+=1
        elif arr[i]<0:
            negative_sum+=1
        else:
            zero+=1
    print(f"{pozitive_sum / n:.6f}")
    print(f"{negative_sum / n:.6f}")
    print(f"{zero / n:.6f}")