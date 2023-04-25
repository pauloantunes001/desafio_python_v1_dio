import textwrap

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques,/):
        
    excedeu_nr_sq = numero_saques >= limite_saques
    if excedeu_nr_sq == True:
        print(f"Limite de quantidade de saques excedido, numero de saques efetuados atualmente: {numero_saques}")
    else:
        if valor > limite:
            print(f"Valor R${valor:.2f} de saque solicitado excede o limite diario permitido")
        elif valor > saldo:
            print(f"Saldo insuficiente\n -Saldo atual: {saldo:.2f}")
        else:
            saldo -=valor
            extrato+= f"Saque: R${valor:.2f} \n"
            numero_saques += 1
        
        return saldo, extrato

def depositar(*, saldo, valor, extrato):
    if valor >= 1:
        saldo += valor  
        extrato += f"Deposito: R${valor:.2f} \n"
    else:
        print("Valor Incorreto")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(f"\n\n========Extrato========== \n{extrato} \n>>> Saldo Atual: R${saldo:.2f}\n================\n\n")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n -> Já existe usuário com esse CPF! ")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("- Usuário criado com sucesso! -")

def criar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n- Conta criada com sucesso! -")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nERRO: Usuário não encontrado, fluxo de criação de conta encerrado! ")

def filtrar_usuario(cpf, usuarios):
    usuario_selecionado = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuario_selecionado[0] if usuario_selecionado else None

def listar_usuario(usuarios):
    for usuario in usuarios:
        print( textwrap.dedent(f"nome:{usuario['nome']}, data_nascimento:{usuario['data_nascimento']}, CPF:{usuario['cpf']}, Endereco:{usuario['endereco']}"))

def listar_contas(contas):
    for conta in contas:
        print( textwrap.dedent(f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """))

def menu():
    menu = """
    [d] Depósito
    [s] Saque
    [e] Extrato
    [nu] Criar User
    [lu] Listar User
    [nc] Criar conta corrente
    [lc] Listar contas
    [q] Sair

    => """
    return input(textwrap.dedent(menu))

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 300
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Insira o valor para Deposito: "))
            saldo, extrato = depositar(saldo=saldo, valor= valor, extrato= extrato)

        elif opcao == "s":        
            valor = float(input("Insira o valor para Saque: "))

            saldo, extrato = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "e":

            exibir_extrato( saldo, extrato= extrato)        
        
        elif opcao == "nu":
            criar_usuario(usuarios)
            
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta_corrente(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lu":
            listar_usuario(usuarios)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Operação Quit - Saindo do programa")
            break

        else:
            print("Operação invalida, por favor selecione uma operação válida")

main()
