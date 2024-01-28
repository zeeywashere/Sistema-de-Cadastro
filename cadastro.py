listas = [[]] #uma lista de lista

while True:
    print("1-Cadastrar pessoa")
    print("2-Lista Cadastros")
    print("3-Procurar Pessoa Especifica")
    op = int(input())#Escolha da opcao
    if op == 1:
        nova = [] # cria uma lista para adicionar o id, nome e idade da pessoa
        nome = input("nome da pessoa:")
        telefone = input("telefone:")
        endereço = input("Endereço")
        nova.append(nome)
        nova.append(telefone)
        nova.append(endereço)
        listas.append(nova)#Adiciona a lista criada com o cadastro da pessoa dentro da lista

    elif op == 2:
        for mostrar in listas:
            for mostrar2 in mostrar:
                print(mostrar2)#mostra tudo dentro da

    elif op == 3:
        print("pensando")