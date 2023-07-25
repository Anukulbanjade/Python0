def multiplication(*abc):
    mul=1
    for i in range(len(abc)):
        mul=abc[i]*mul
    return print(mul)

multiplication(7,8,9)