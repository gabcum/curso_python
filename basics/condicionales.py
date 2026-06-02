###
#Sentencias simples condicionales (if, elif, else) 
###

import os 

os.system("clear") #Limpiar la consola para mejor visualización

edad = 17

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

###Sentencia Elif (else if) para evaluar múltiples condiciones
nota = 7
if nota >=9:
    print("Excelente")
elif nota >= 7:
    print("Aprobado")
else:
    print("Reprobado")

###Condiciones multiples 

edad = 25
tiene_licencia = True
if edad >=25 and tiene_licencia:
    print("Puedes alquilar un coche")
else:    
    print("Policia!!")

#Un pueblo
edad = 25
tiene_licencia = False
if edad >= 18 or tiene_licencia:
    print("Puedes Conducir")
else: 
    print("No puedes conducir")

### Darle la vuelta a una condición con not
es_fin_de_semana = False
if not es_fin_de_semana:
    print("Tengo que trabajar")
else:
    print("Es fin de semana, a descansar")

###Anidar condiciones
edad = 20
tiene_dinero = True
if edad >= 18:
    if tiene_dinero:
        print("Puedes salir a divertirte")
    else:
        print("No tienes dinero para salir")
else:
    print("Eres menor de edad, no puedes salir")

#Simplificando condicion anterior sin anidar 
edad = 20
tiene_dinero = True
if edad < 18:
    print("Eres menor de edad, no puedes salir")
elif tiene_dinero:
    print("Puedes salir a divertirte")
else:
    print("No tienes dinero para salir")
