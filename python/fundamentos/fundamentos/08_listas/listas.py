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