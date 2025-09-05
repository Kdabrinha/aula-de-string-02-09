frase= "infoco consultoria e treinamentos"
print(len(frase))#mostra o tamanho da frase

print(frase[7])

print(frase[7:18])

print(frase[7:18:2])

print(frase[: 5])

print(frase[21:])

print(frase.count("o"))

print(frase.find("tre"))

print(frase.find("etec"))

print("etec" in frase) #pergunta se tem etec na frase

print(frase.replace("infoco", "lindolfo"))#troca

print(frase.upper())#deixa a frase em maiusculo

print(frase.lower())#deixa a frase em minusculo

print(frase.capitalize()) #primeira letra maiuscula e as outras minusculas

print(frase.title()) #primeira letra de cada palavra em maiuscula

print(50*"=")

nome = "    lindolfo J   - "
nomeok=nome.strip()
print(nome)
print(len(nome))

print(8*".")

print(nomeok)
print(len(nome))
 

print(nome.rstrip())
print(nome.lstrip())



print(50*"=")

frase2= frase.split()
print(frase2)


print(frase2[1])
print(frase2[1][3])

print(8*".")

print("-".join(frase2))