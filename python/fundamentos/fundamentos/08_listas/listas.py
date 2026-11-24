lista_vacia = [] #Listas, array, Matriz
lista_compras = ['tomate', 'pan', 'queso', 'jamón']

lista_especial = [1, 2, ['a', 'b', 'c'], True]

verso1 = ['dale', 'a', 'tu', 'cuerpo',]
verso2 = ['alegria', 'macarena']
estrofa = verso1 + verso2
print(estrofa)
cancion = 3 * estrofa
print(cancion)
#A traves de concatenacion y multiplicacion de listas,
#escribe la cancion "Dale a tu cuerpo alegria macarena" completa.

#Cancion Macarena:
coro = ['dale', 'a', 'tu', 'cuerpo', 'alegría,', 'Macarena,',
        'que', 'tu', 'cuerpo', 'es', 'pa', 'darle', 'alegría', 'y', 'cosa', 'buena',
        'Dale', 'a', 'tu', 'cuerpo', 'alegría', 'Macarena',
        'Eh,', 'Macarena', '(¡ay!)']
estrofa = ['Macarena', 'tiene', 'un', 'novio', 'que', 'se', 'llama',
            'Que', 'se', 'llama', 'de', 'apellido', 'Vitorino',
            'Y', 'en', 'la', 'jura', 'de', 'bandera', 'del', 'muchacho',
            'Se', 'la', 'dio', 'con', 'dos', 'amigos', '(¡ay!)']
cancionMacarena = [2 * coro + 2 * estrofa]
print(cancionMacarena)

#Condicion if-else
numero1 = 70
if numero1 > 45:
    pass
else:
    print("Numero menor")

cajonera = ["pantalones", "camisetas", "calcetines"]
print(cajonera[0])
print(cajonera[1])
print(cajonera[2])
cajonera[1] = "sueters"
print(cajonera)

cajonera.append("vestidos")
print(cajonera)

#Añadir 4 elementos mas a la cajonera.
cajonera.append("polerones")
cajonera.append("poleras")
cajonera.append("buzos")
cajonera.append("jeans")
print(", ".join(cajonera))

lista_grande = [2, 4, 6, 8, 10, 12, 14, 16]
print(lista_grande[3:]) #Imprime 8 10 12 14 16
print(lista_grande[:6]) #Imprime hasta el 6
print(lista_grande[3:6]) #Imprime desde el 3 hasta el 6

# Ejercicio: Crear una lista de numeros del 3 al 30
# De 3 en 3 y utilizar slicing para imprimir los
# Siguientes numeros.
# 1.- Entre 9 y 15
# 2.- Superiores a 21
# 3.- Inferiores a 18
# 4.- Entre 15 y 27

lista_tarea = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
print(lista_tarea [3:5])
print(lista_tarea [7:])
print(lista_tarea [:6])
print(lista_tarea [5:9])

vocales = ['a', 'e', 'i', 'o', 'u']
print(len(vocales))

numerosAleatorios = [2, 20, 5, 33, 1, 67]
print("Largo de variales es: ", len(numerosAleatorios))
print("Numero mas alto: ", max(numerosAleatorios))
print("Numero mas bajo: ", min(numerosAleatorios))
print("Lista ordenada: ", sorted(numerosAleatorios))

frozen = ["Elsa", "Anna", "Olaf"]
frozen.pop()
print(frozen)

listaSeries = ["One Piece", "Given", "Slam Dunk", "Chavo del 8",
                "The Bigbang Theory", "Happy tree Friends",
                "Soy luna", "The Simpsons"]