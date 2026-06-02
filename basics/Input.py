'''
print("Hola, como te llamas: ")
nombre = input()
print(nombre)
'''
###Impresion directa en input 
nombre = input("Hola, como te llamas: \n")
print(f"Hola, {nombre}!") 

###Convertir el string a entero para poder hacer la suma
age = input("Cuantos años tienes: \n")
print(f"dentro de 10 años tendrás {int(age) + 10} años")  


###Split para obtener multiples datos en una sola linea
print("Obtener multiples datos")
country, city = input("De que país y ciudad eres: \n").split() ###Separar por espacio las respuestas y asignarlas a las variables
print(f"Vives en {city}, {country}")