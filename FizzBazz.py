for i in range(1,101):
    n = ''
    if (i % 3 == 0):
        n = 'Fizz'
    if (i % 5 == 0):
        n = 'Buzz'
    if (i % 15 == 0):
        n = 'FizzBuzz'
    # if (i % 2 == 0):
    #     s = s + 'GLEB'
    # чтобы вывести и все остальные числа
    # if not n:
    #     n = n+str(i)
    print (n)