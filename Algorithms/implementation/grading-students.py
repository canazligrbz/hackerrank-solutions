def gradingStudents(grades):
    result=[]
    for i in grades:
        if i<38:
            result.append(i)
        else:
            if i%5>=3:
                result.append(i+(5-(i%5)))
            else:
                result.append(i)
    return result