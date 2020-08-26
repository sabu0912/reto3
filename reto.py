#CADA UNA DE LAS NOTAS 
while True:
    try:
     nota1 = int(input("Ingresa la primera nota : "))
     print(f"La primera nota es :", (nota1))
     nota2 = int(input("Ingresa la segunda nota : "))
     print(f"La segunda nota es :", (nota2))
     nota3 = int(input("Ingresa la tercera nota : "))
     print(f"La tercera nota es :", (nota3))    
     nota4 = int(input("Ingresa la cuarta nota : "))
     print(f"La cuarta nota es :", (nota4))     
     nota5 = int(input("Ingresa la quinta nota : "))
     print(f"La quinta nota es :", (nota5))
     break
    except Exception:
        print("El valor de la nota NO es numerico")

lista_notas = []
lista_notas.append(nota1)
lista_notas.append(nota2)
lista_notas.append(nota3)
lista_notas.append(nota4)
lista_notas.append(nota5)
lista_notas: [nota1,nota2,nota3,nota4,nota5]
print(f"La lista de nota es : {lista_notas}")

#NOTA DE MENOR A MAYOR
lista_desordenada = lista_notas
lista_desordenada.sort()
print(f"La nota de menor a mayor es : {lista_desordenada}")

#NOTA DE MAYOR A MENOR
lista_al_reves = lista_desordenada[::-1]
print(f"La nota de mayor a menor es : {lista_al_reves}")

#NOTA PROMEDIO
nota_promedio = nota1+nota2+nota3+nota4+nota5 // 5
print(f"La nota promedio es : {nota_promedio}")


'''#NOTA MAYOR
print(lista_notas)
nota_mayor = lista_notas[0]

for i in range(0,len(lista_notas)):
    if lista_notas[i]>nota_mayor:
        nota_mayor = lista_notas[i]
print("La nota mayor es : ",nota_mayor)
print("La posición que ocupa la nota es: ",lista_notas.index(nota_mayor))


#NOTA MENOR
print(lista_notas)
nota_menor = lista_notas[0]

for i in range(0,len(lista_notas)):
    if lista_notas[i]<nota_menor:
        nota_menor = lista_notas[i]
print("La nota menor es : ",nota_menor)
print("La posición que ocupa la nota es: ",lista_notas.index(nota_menor))


#NOTA PROMEDIO
print(lista_notas)
suma = 0

for i in lista_notas:
    sum = i
promedio = suma / i
print("La nota promedio es :",nota_promedio)'''

