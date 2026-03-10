strings = ['a','b','c','d']
# 4*4 = 16 bytes of storage is used

print(strings[2])

# push
# Adiciona no final do array
strings.append('e') # O(1)

print(strings)

# drop
# Remove o último item do array
strings.pop() # O(1)

print(strings)

# Adicionando um item no início do array
strings.insert(0, 'x') # O(n)
print(strings)

# Adicionando um item no meio do array
strings.insert(2, 'y') # O(n)
print(strings)

nome=input("Digite seu nome: ")