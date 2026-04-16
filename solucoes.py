def sao_anagramas(string1, string2):
    # Converter para minúsculas e remover espaços
    s1 = string1.lower().replace(" ", "")
    s2 = string2.lower().replace(" ", "")
    
    # Comparar as letras ordenadas
    return sorted(s1) == sorted(s2)
    

def cifra_de_cesar(texto, deslocamento):
    # TODO: Implemente a logica
    pass
    

def valida_cpf(cpf_string):
    # TODO: Implemente a logica
    pass
    