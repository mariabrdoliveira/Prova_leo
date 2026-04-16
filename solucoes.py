import string

def sao_anagramas(string1, string2):
    # Converter para minúsculas e remover espaços
    primeiro_texto = string1.lower().replace(" ", "")
    segundo_texto = string2.lower().replace(" ", "")
    
    # Comparar as letras ordenadas
    return sorted(primeiro_texto) == sorted(segundo_texto)
    

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