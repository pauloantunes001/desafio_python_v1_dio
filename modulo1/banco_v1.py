menu = """
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 300
extrato= ""
numero_saques = 0
LIMITE_SAQUE= 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Operação Déposito")
        valor = float(input("Insira o valor para Deposito"))

        if valor >= 1:
            saldo += valor  
            extrato += f"Deposito: R${valor:.2f} \n"
        else:
            print("Valor Incorreto")
    
    elif opcao == "s":
        print("Operação Saque")
        
        excedeu_nr_sq = numero_saques >= LIMITE_SAQUE
        if excedeu_nr_sq == True:
            print(f"Limite de quantidade de saques excedido, numero de saques efetuados atualmente: {numero_saques}")
        else:
            valor = float(input("Insira o valor para Saque"))
            if valor > 500:
                print(f"Valor R${valor:.2f} de saque solicitado excede o limite diario permitido")
            elif valor > saldo:
                print(f"Saldo insuficiente\n -Saldo atual: {saldo:.2f}")
            else:
                saldo -=valor
                extrato+= f"Saque: R${valor:.2f} \n"
                numero_saques += 1

    elif opcao == "e":
        print(f"\n\n========Extrato========== \n{extrato} \n>>>Saldo Atual: R${saldo:.2f}\n================\n\n")
    
    elif opcao == "q":
        print("Operação Quit - Saindo do programa")
        break
    
    else:
        print("Operação inválida, por favor selecione uma operação válida")
