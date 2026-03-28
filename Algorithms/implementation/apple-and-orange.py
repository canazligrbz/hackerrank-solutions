def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_result = []
    oranges_result = []
    for i in apples:
        apples_result.append(a + i)
    for j in oranges:
        oranges_result.append(b + j)

    apples_sum = 0
    oranges_sum = 0

    for x in apples_result:
        if x <= t and x >= s:
            apples_sum += 1

    for y in oranges_result:
        if y <= t and y >= s:
            oranges_sum += 1

    print(apples_sum)
    print(oranges_sum)
