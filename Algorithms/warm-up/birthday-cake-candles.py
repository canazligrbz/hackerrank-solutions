def birthdayCakeCandles(candles):
    sum_candles=0
    x= max(candles)
    for i in candles:
        if x==i:
            sum_candles+=1
    return sum_candles