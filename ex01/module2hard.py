def password(number: int) -> str:
    stroka = ""
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                stroka += str(i) + str(j)
    return stroka
