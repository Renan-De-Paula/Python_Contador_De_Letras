# Solicita ao usuário uma frase, remove espaços nas pontas e converte para letras maiúsculas
frase = str(input("Escreva a frase: ")).strip().upper()

# Solicita ao usuário o caractere a ser procurado, aplica strip e converte para maiúsculo
letra = str(input("qual caracter voce quer procurar? ")).strip().upper()

# Exibe quantas vezes o caractere aparece na frase
print("{} tem tanta letra {}: {} ".format(frase, letra, frase.count(letra)))

# Exibe a posição da primeira ocorrência da letra (+1 para considerar posição humana)
print(" a letra {}, apareceu na posiçao: {}".format(letra, frase.find(letra) + 1))

# Exibe a posição da última ocorrência da letra (+1 para considerar posição humana)
print("a ultima posiçao da {}, foi {}".format(letra, frase.rfind(letra) + 1))
