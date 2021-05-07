from Conta import Conta
from Extrato import Extrato
from Cliente import Cliente

resp = ""
users = []
accs = []
id_user = -1


while resp != "nao":

    erro = True
    found = False

    resp = input("Deseja realizar qual operação? ")

    if (resp == "cliente"):

        nome = input("Qual seu nome? ")

        while erro == True:
            try:
                cpf = int(input("Qual seu cpf (somente numeros)? "))
                erro = False

            except:
                print("Opa! Digite somente números!")
                erro = True

        end = input("Qual seu endereço? ")
        user = Cliente(nome, cpf, end)
        users.append(user)

        print("Confirme suas informações:")
        print(f'\nNome: {nome}\nCpf: {cpf}\nEndereço: {end}\n')
        correto = input("Correto(s/n)? ")
        if correto == "s":
            id_user += 1
            print(f'Ok! Perfil criado com sucesso com a ID:{id_user}')
            verif = input("Gostaria de verificar as informações? ")
            if (verif == "s"):
                print(f'\nNome: {nome}\nCpf: {cpf}\nEndereço: {end}\n')

            elif (verif == "n"):
                continue

            else:
                print("Não entendemos sua resposta. Continuando...")
                continue

        elif correto == "n":
            continue

        else:
            print("Não entendemos sua resposta. Continuando...")
            continue

    elif (resp == "mostrar"):

        for u in range(len(users)):
            print(f'Nome: {users[u].nome} | CPF: {users[u].cpf} | Endereço: {users[u].endereco}')

    elif (resp == "pesquisa cliente"):
        pesq_input = input("Deseja pesquisar utilizando qual dado? ")
        if (pesq_input == "nome"):
            pesq_nome = input("Digite o nome para busca: ")
            while (found == False):
                for u in range(len(users)):
                    if pesq_nome in users[u].nome:
                        found = True
                        print(f'Dados do usuário encontrado:')
                        print(f'Nome: {users[u].nome} | CPF: {users[u].cpf} | Endereço: {users[u].endereco}')
                    else:
                        pass
                print("Nenhum usuário encontrado.")
            continue
        elif (pesq_input == "cpf"):
            pesq_cpf = input("Digite o cpf para busca: ")
            while (found == False):
                for u in range(len(users)):
                    if (eval(pesq_cpf) == users[u].cpf):
                        found = True
                        print(f'Dados do usuário encontrado:')
                        print(f'Nome: {users[u].nome} | CPF: {users[u].cpf} | Endereço: {users[u].endereco}')
                    else:
                        pass
                if (found == False):
                    print("Nenhum usuário encontrado.")
            continue
        elif (pesq_input == "id"):
            try:
                pesq_id = int(input("Digite o ID para busca: "))
                print(f'Dados do usuário encontrado:')
                print(f'Nome: {users[pesq_id].nome} | CPF: {users[pesq_id].cpf} | Endereço: {users[pesq_id].endereco}')
            except:
                print("Nenhum usuário encontrado.")

    elif (resp == "conta"):
        #ao colocar o try identar o codigo abaixo
        try:
            resp_cliente = int(input("Digite o número de identificação do cliente: "))
            acc = Conta(users.index(users[resp_cliente]), 0)
            acc.clientes.append(users[resp_cliente])
            accs.append(acc)
            print("Conta criada com sucesso.")
            resp_conta = input("Deseja adicionar outro cliente para esta conta? ")
            while resp_conta == "s":
                print(accs[users.index(users[resp_cliente])].clientes)
                resp_cliente2 = int(input("Digite o número de identificação do outro cliente: "))
                accs[users.index(users[resp_cliente])].clientes.append(users[resp_cliente2])
                print("Adicionado com sucesso.")
                print(accs[users.index(users[resp_cliente])].clientes)
                resp_conta = input("Deseja adicionar outro cliente para esta conta? ")
        except:
            print("Erro.")

    elif (resp == "pesquisa conta"):

        try:
            pesq_input = int(input("Qual o número da conta que deseja consultar? "))
            print(f'\nNúmero da conta: {accs[pesq_input].numero}\n')
            print("Clientes: ")
            for i in range(len(accs[pesq_input].clientes)):
                print(f'Nome: {accs[pesq_input].clientes[i].nome} | CPF: {accs[pesq_input].clientes[i].cpf}')
            print(f'\nSaldo: {accs[pesq_input].saldo}\n')
        except:
            print("Erro.")