# Reto_8
Por: Juan Diego Cárdenas Olarte
### Grupo: 
#### Infinity Bit Team (∞BT)

[![logo.jpg](https://i.postimg.cc/pdcVKPsT/logo.jpg)](https://postimg.cc/JyJWLCVV)

Este reto contiene las actividades propuestas para el reto#6.

>### Punto 1.
>Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

El codigo a usar es el siguiente:

```python
for numero in range(1,101): 
    cuadrado:int=numero**2
    print(numero)
    print(cuadrado)
```
>### Punto 2.
>Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

El codigo a usar es: 

```python
for numero in range(1,1000,2):
    print(numero)
for numero in range(2,1001,2): 
    print(numero)
```
>### Punto 3.
>Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado.

El codigo a usar es el siguiente:

```python
numero:int=int(input("escriba un número mayor o igual a 2: "))
if numero % 2 !=0:
     numero -= 1
for i in range(numero,1,-2): print(i)
```
>### Punto 4.
>Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial.

El codigo a usar es el siguiente:
```python
numero:int=int(input("escriba un número: "))
for i in range(1,numero+1):
    factorial : int = 1
    for i in range(1, i+1):
        factorial *= i
    print(i)
    print(factorial)
```
>### Punto 5.
>Calcular el valor de 2 elevado a la potencia n usando ciclos for.

El codigo a usar es el siguiente.

```python
numero:int=int(input("escriba un número: "))
potencia : int = 1
for i in range(1, numero+1):
        potencia *= 2
print(potencia)
```
>### Punto 6.
>Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).

El codigo a usar es el siguiente:

```python
numero_n:int=int(input("Escriba un número natural: "))
numero_x=float(input("Escriba un número real: "))
potencia : int = 1
for i in range(1, numero_n+1):
        potencia *= numero_x
print(potencia)
```
>### Punto 7.
>Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

El codigo a usar es el siguiente:

```python
numero=int(input("Escribe un numero del 1 al 9: "))
for multiplicar in range (1,11):
    tablas=numero*multiplicar
    print(tablas)
```

>### Punto 8.
>Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

>### Punto 9.
>Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

>### Punto 10.
>Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
