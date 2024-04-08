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
for numero in range(1,101): #Para cada numero dentro del rango (1-100)
    cuadrado:int=numero**2 #Elevar el numero al cuadrado
    print(numero) # Imprimir el numero
    print(cuadrado) # Imprimir el cuadrado del numero
```
>### Punto 2.
>Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

El codigo a usar es: 

```python
for numero in range(1,1000,2): #Para cada numero de 1 a 999 cada dos numeros
    print(numero) #Imprimir numero
for numero in range(2,1001,2): #Para cada numero de 2 a 1000 cada dos numeros
    print(numero) #Imprimir numero
```
>### Punto 3.
>Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado.

El codigo a usar es el siguiente:

```python
numero:int=int(input("escriba un número mayor o igual a 2: ")) #Se declara e inicializa una variable a traves de la consola
if numero % 2 !=0: #Condiciona que si "numero" es impar se le resta uno.
     numero -= 1
for i in range(numero,1,-2): #Para cada numero en el rango (numero a 1) restar de a 2
print(i) #Imprimir cada numero.
```
>### Punto 4.
>Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial.

El codigo a usar es el siguiente:
```python
numero:int=int(input("escriba un número: ")) #Se declara e inicializa una variable a traves de la consola
for i in range(1,numero+1): #Para cada numero en el inervalo 1 a numero hacer
    factorial : int = 1 #Se inicializa y declara una variable con valor 1
    for i in range(1, i+1): #Para cada valor en un rango de 1 hasta i+1
        factorial *= i #Multiplicar factorial por cada valor de i
    print(i) #Imprimir el numero
    print(factorial) #Imprimir su respectico factorial
```
>### Punto 5.
>Calcular el valor de 2 elevado a la potencia n usando ciclos for.

El codigo a usar es el siguiente.

```python
numero:int=int(input("escriba un número: ")) #Se declara e inicializa una variable a traves de la consola
potencia : int = 1 #Se inicializa y declara una variable con valor 1
for i in range(1, numero+1):  #Para cada numero en el inervalo 1 a numero hacer
        potencia *= 2 # Multiplicar por 2
print(potencia) #Imprimir el resultado
```
>### Punto 6.
>Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).

El codigo a usar es el siguiente:

```python
numero_n:int=int(input("Escriba un número natural: "))  #Se declara e inicializa una variable "numero_n" a traves de la consola
numero_x=float(input("Escriba un número real: "))  #Se declara e inicializa una variable "numero_x" a traves de la consola
potencia : int = 1  #Se inicializa y declara una variable con valor 1
for i in range(1, numero_n+1): #Para cada numero en el inervalo 1 a numero hacer
        potencia *= numero_x # Se multiplica por "numero"
print(potencia) #Imprimir el resultado.
```
>### Punto 7.
>Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

El codigo a usar es el siguiente:

```python
numero=int(input("Escribe un numero del 1 al 9: "))  #Se declara e inicializa una variable "numero_n" a traves de la consola
for multiplicar in range (1,11): #Para cada numero en el intervalo 1-11 hacer
    tablas=numero*multiplicar #Se multiplica por "numero"
    print(tablas) #Se imprime la tabla del numero seleccionado
```

>### Punto 8.
>Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

>### Punto 9.
>Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

>### Punto 10.
>Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
