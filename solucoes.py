import string

def sao_anagramas(string1, string2):
    # Converter para minúsculas e remover espaços
    primeiro_texto = string1.lower().replace(" ", "")
    segundo_texto = string2.lower().replace(" ", "")
    
    # Comparar as letras ordenadas
    return sorted(primeiro_texto) == sorted(segundo_texto)
    

def cifra_de_cesar(texto, deslocamento):
    resultado = ""
    for c in texto:
        if 'a' <= c <= 'z':
            resultado += chr((ord(c) - ord('a') + deslocamento) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            resultado += chr((ord(c) - ord('A') + deslocamento) % 26 + ord('A'))
        else:
            resultado += c  # Mantem espaços, numeros e pontuacao
    
    return resultado
    

def encontrar_maior_palavra(frase):
    palavras = frase.split()
    palavras_limpas = [p.strip(string.punctuation) for p in palavras]
    return max(palavras_limpas, key=len)


if __name__ == "__main__":
    frase = input("Digite a sua frase: ")
    print(encontrar_maior_palavra(frase))