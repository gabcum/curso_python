### Strings ### 
my_string = "This is a string"
my_string2 = 'This is also a string'
print(my_string) 
print(len(my_string)) #len() cuenta los caracteres de la cadena
print(my_string2)
print(len(my_string2)) #len() cuenta los caracteres de la cadena

print(my_string + " " + my_string2) #Concatenacion de strings

my_new_line_string = "This is a string\nwith a new line" 
print(my_new_line_string) #\n es un caracter de escape que crea una nueva linea

my_tab_string = "This is a string\twith a tab"
print(my_tab_string) #\t es un caracter de escape que crea una tabulacion

my_scape_string = "\\tThis is a string with a \"double quote\" and a \\n'single quote\'"
print(my_scape_string) #\" es un caracter de escape que permite usar comillas dobles dentro de una cadena

## Formateo de strings
print("mi nombre es Gabriel y tengo 25 años") #Forma tradicional de concatenar strings
name, age = "Gabriel", 25
print("mi nombre es {} y tengo {} años".format(name, age)) #Forma de formateo de strings con format()
print("mi nombre es {0} y tengo {1} años".format(name, age)) #Forma de formateo de strings con format() usando indices
print("mi nombre es %s y tengo %d años" % (name, age)) #Forma de formateo de strings con el operador % (antigua forma de formateo de strings)
print(f"mi nombre es {name} y tengo {age} años") #Forma de formateo de strings con f-strings (Python 3.6+)


### Desempaquetado de strings
language = "python"
a, b , d, e, f, g = language
print(a) #P
print(b) #y


###Division de strings
language_slice = language[1:4] #slice de string, toma los caracteres desde el indice 1 hasta el indice 3 (el indice 4 no se incluye)
print(language_slice) 
language_slice = language[1:] #slice de string, toma los caracteres desde el indice 1 hasta el final de la cadena
print(language_slice) 
language_slice = language[0:6:2] #slice de string, toma los caracteres desde el indice 0 hasta el indice 5 (el indice 6 no se incluye) con un paso de 2 (toma un caracter y salta el siguiente)
print("prueba: " + language_slice)



####Reversar un string
reversed_language = language[::-1] #slice de string, toma los caracteres desde el final hasta el principio de la cadena
print(reversed_language)


###Funciones de strings
print(language.capitalize()) #Capitaliza la primera letra de la cadena
print(language.upper()) #Convierte la cadena a mayusculas
print(language.count("o")) #Cuenta el numero de veces que aparece el caracter "o"
print(language.isnumeric()) #Devuelve True si la cadena es un numero, False en caso contrario
print("1".isnumeric()) #Devuelve True si la cadena es un numero, False en caso contrario
print(language.lower()) #Convierte la cadena a minusculas
print(language.upper().isupper()) #Convierte la cadena a mayusculas y luego verifica si la cadena esta en mayusculas, devuelve True si es asi, False en caso contrario
print(language.startswith("py")) #Devuelve True si la cadena empieza con "py", False en caso contrario