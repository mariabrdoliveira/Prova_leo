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
    

def valida_cpf(cpf_string):
    # TODO: Implemente a logica
    pass
    