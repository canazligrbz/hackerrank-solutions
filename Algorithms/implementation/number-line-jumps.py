def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return ("NO")

    jump = ((x2 - x1) / (v1 - v2))
    kalan = ((x2 - x1) % (v1 - v2))

    if jump >= 0 and kalan == 0:
        return ("YES")
    else:
        return ("NO")


# İkinci çözüm:

def kangaroo2(x1, v1, x2, v2):
    if v1 > v2:
        if (x2 - x1) % (v1 - v2) == 0:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"