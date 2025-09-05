n=input("Digite seu nome->").strip().upper()


qa=n.count("A")

pp=n.find("A")

up=n.rfind("A")

print("O nome tem", qa, "letras A")
print(20*".")

print("A primeira letra A aparece na posição", pp +1 )
print(20*".")

print("A ultima letra A aparece na posição", up+1 )


