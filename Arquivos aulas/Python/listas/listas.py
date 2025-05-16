# renomeando um elemento

frutas = ["uva", 'kiwi', 'maca', 'caqui']

print(frutas[2])
frutas[2] = 'laranja'
print(frutas)

# remover elemento e retorna o elemento

remove = frutas.pop(1)
print(frutas)

# deletar literal

del frutas[0]
print(frutas)

# tentativa de renome

frutas[2] = 'banana'