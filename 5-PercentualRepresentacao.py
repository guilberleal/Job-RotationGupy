# Define a string a ser invertida
string = "Exemplo de string a ser invertida"

# Inicializa uma lista vazia para armazenar cada caractere da string
lista_caracteres = []

# Itera sobre a string, adicionando cada caractere à lista
for caractere in string:
    lista_caracteres.append(caractere)

# Inverte a ordem dos caracteres na lista
lista_caracteres.reverse()

# Concatena os caracteres na lista para formar a string invertida
string_invertida = "".join(lista_caracteres)

# Imprime a string invertida
print(string_invertida)
