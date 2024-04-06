num:int=int(input("escriba un número mayor o igual a 2: "))
if num%2!=0:
     num-=1
for n in range(num,1,-2): print(n)