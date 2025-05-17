
def formar_duplas(nomes):
    for i in range(len(nomes)):
        for j in range(i + 1, len(nomes)):
            print(f"{nomes[i]} e {nomes[j]}")

nomes = ("Ana", "Bia", "Celi", "Diana", "Eva", "Fabia")
formar_duplas(nomes)
