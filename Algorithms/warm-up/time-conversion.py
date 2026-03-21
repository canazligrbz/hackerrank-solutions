def timeConversion(s):
    hour = int(s[:2])
    rest = s[2:8]
    period = s[8:]

    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0


    return f"{hour:02d}{rest}"