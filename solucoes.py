import string

def sao_anagramas(string1, string2):
    # TODO: Implemente a logica
    pass
    

def cifra_de_cesar(texto, deslocamento):
    # TODO: Implemente a logica
    pass
    

def encontrar_maior_palavra(frase):
    palavras = frase.split()
    palavras_limpas = [p.strip(string.punctuation) for p in palavras]
    return max(palavras_limpas, key=len)


if __name__ == "__main__":
    frase = input("Digite a sua frase: ")
    print(encontrar_maior_palavra(frase))