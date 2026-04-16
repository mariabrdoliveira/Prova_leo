def sao_anagramas(string1, string2):
    # Converter para minúsculas e remover espaços
    primeiro_texto = string1.lower().replace(" ", "")
    segundo_texto = string2.lower().replace(" ", "")
    
    # Comparar as letras ordenadas
    return sorted(primeiro_texto) == sorted(segundo_texto)
    

def cifra_de_cesar(texto, deslocamento):
    # TODO: Implemente a logica
    pass
    

def valida_cpf(cpf_string):
    # TODO: Implemente a logica
    pass
    