
# se palavra = 'argentina' return _ _ _ _ _ _ _ _ _
def get_palavra_secreta(palavra: str) -> str:

    resp = ""
    for c in palavra:
        palavra.replace
        resp = resp + "_ "
    return resp

def substitui(frase: str, letra: str,) -> str:
    resp = ""
    for c in frase:
        if c == letra:
            resp = resp + c + "* "
        else:
            resp = resp + "_ "
        return resp


if __name__ == "__main__":
    palavra = "Espanha"
    segredo = get_palavra_secreta(palavra)
    print(segredo)
    letra = input("Letra: ")[0]

    aux = substitui(palavra, letra)
    print(aux)

