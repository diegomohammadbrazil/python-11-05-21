frase = input('Digite uma frase: ').lower()
vogais = "aeiou"
for i in vogais:
    frase = frase.replace(i, '')

print(frase)