'''precos = [2000,1000,5000,6000]
with open("precos_roupas.txt", "w") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')
print(arquivo.closed)
precos = [10000]
with open("precos_roupas.txt", "a") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')'''

disciplinas = ["RAD \n", "Introducao 7ai km "]
with open("disciplinas.txt", "w") as file:
    file.write("Relacao e disciplinas")
    file.writelines(disciplinas)