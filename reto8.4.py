numero:int=int(input("escriba un número: "))
for i in range(1,numero+1):
    factorial : int = 1
    for i in range(1, i+1):
        factorial *= i
    print(i)
    print(factorial)