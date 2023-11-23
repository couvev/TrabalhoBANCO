from classes import Cliente, Conta, Extrato, Historico
import random
from datetime import datetime
import time
import pickle
import os

def salvar_dados():
    dados = {'num_contas': num_contas, 'contas': contas, 'clientes': clientes, 'historico': historico}
    with open('dados_bancarios.txt', 'wb') as arquivo:
        pickle.dump(dados, arquivo)

def carregar_dados():
    try:
        with open('dados_bancarios.txt', 'rb') as arquivo:
            if os.path.getsize('dados_bancarios.txt') > 0:
                dados = pickle.load(arquivo)
                return dados['num_contas'], dados['contas'], dados['clientes'], dados['historico']
            else:
                return [], [], [], []
    except FileNotFoundError:
        return [], [], [], []

def main():
    
    global num_contas, contas, clientes, historico
    num_contas, contas, clientes, historico = carregar_dados()
    
    opcao = 0
    while opcao != -1:
        
        time.sleep(3)
        
        print("\n|==================================================|\n"
                "|        BEM-VINDO, O QUE VOCÊ DESEJA FAZER?       |\n"
                "|==================================================|\n"
                "| 1 - Adicionar cliente e conta                    |\n"
                "| 2 - Ver informações de todas as contas           |\n"
                "| 3 - Ver informações de uma conta                 |\n"
                "| 4 - Depositar na conta                           |\n"
                "| 5 - Sacar da conta                               |\n"
                "| 6 - Transferir de uma conta para outra           |\n"
                "| 7 - Imprimir extrato de uma conta                |\n"
                "| 8 - Imprimir histórico do sistema                |\n"
                "|==================================================|\n"
                "| -1 - Encerrar programa                           |\n"
                "|==================================================|\n\n")

        opcao = int(input("Qual comando você deseja executar? "))
        
        if opcao == 1:
            nome = input("\n\nQual é o nome desse cliente? ")
            cpf = input("Qual é o CPF desse cliente? ")
            saldo = float(input("Qual será o saldo inicial da conta? "))
            while True:
                numero_conta = random.randint(1000, 9999)
                if numero_conta not in num_contas:
                    break
            print(f"Numero da nova conta: {numero_conta}")
            
            num_contas.append(numero_conta)

            cliente_atual = Cliente(nome, cpf)
            clientes.append(cliente_atual)
            
            conta_atual = Conta(cpf, numero_conta, saldo)
            contas.append(conta_atual)
            
            data_hora_atual = datetime.now()
            data_hora_formatada = data_hora_atual.strftime("%d-%m-%Y %H:%M:%S")

            info = f"Conta criada com saldo de R$:{saldo}!"
            extrato = Extrato(data_hora_formatada, info)

            conta_atual.adicionar_extrato(extrato)
            
            h_info = f"Conta {numero_conta} criada."
            h = Historico(data_hora_formatada,h_info)
            historico.append(h)
        
        elif opcao == 2:
            for cliente in clientes:
                for conta in contas:
                    if conta.cpf == cliente.cpf:
                        print(f"\n\nNome do cliente: {cliente.nome}\nCPF: {cliente.cpf}\nNumero da conta: {conta.numero}\nSaldo: {conta.saldo}")
            
            data_hora_atual = datetime.now()
            data_hora_formatada = data_hora_atual.strftime("%d-%m-%Y %H:%M:%S")
                        
            h_info = f"Informações de todas as contas printadas."
            h = Historico(data_hora_formatada,h_info)
            historico.append(h)
         
        elif opcao == 3:
            forma = int(input("Buscar via:\n1 - CPF\n2 - Numero da conta\n- "))
            
            if forma == 1:
                cpf_desejado = input("\nDigite o numero do CPF desejado: ")
                cpf_encontrado = None
                
                data_hora_atual = datetime.now()
                data_hora_formatada = data_hora_atual.strftime("%d-%m-%Y %H:%M:%S")
                        
                h_info = f"Busca feita no CPF: {cpf_desejado}."
                h = Historico(data_hora_formatada,h_info)
                historico.append(h)

                for cliente in clientes:
                    if str(cliente.cpf) == cpf_desejado:
                        cpf_encontrado = cliente
                        break 

                if cpf_encontrado:
                    for conta in contas:
                        if conta.cpf == cpf_encontrado.cpf:
                            print(f"\n\nNome do cliente: {cpf_encontrado.nome}\nNumero da conta: {conta.numero}\nSaldo: {conta.saldo}")
                else:
                    print("\nNenhuma informação encontrada ou CPF inexistente.") 
                        
            elif forma == 2:
                conta_desejada = input("\nDigite o numero da conta desejada: ")
                conta_encontrada = None
                
                data_hora_atual = datetime.now()
                data_hora_formatada = data_hora_atual.strftime("%d-%m-%Y %H:%M:%S")
                        
                h_info = f"Busca feita na conta: {conta_desejada}."
                h = Historico(data_hora_formatada,h_info)
                historico.append(h)
                
                for conta in contas:
                    if str(conta.numero) == conta_desejada:
                        conta_encontrada = conta
                        break

                if conta_encontrada:
                    for cliente in clientes:
                        if cliente.cpf == conta_encontrada.cpf:
                            print(f"\n\nNome do cliente: {cliente.nome}\nCPF: {cliente.cpf}\nSaldo: {conta_encontrada.saldo}")
                else:
                    print("\nNenhuma informação encontrada ou conta inexistente.") 
                           
         
        elif opcao == 4:
            conta_destino = input("Número da conta destino: ")
            valor_transferencia = float(input("Valor a ser depositado: "))

            conta_encontrada = None

            for conta in contas:
                if str(conta.numero) == conta_destino:
                    conta_encontrada = conta
                    break

            if conta_encontrada:
                conta_encontrada.saldo += valor_transferencia
                print(f"Deposito de R$:{valor_transferencia:.2f} para a conta {conta_encontrada.numero} realizado com sucesso.")
                print(f"Saldo atual: R$:{conta_encontrada.saldo}")
                
                data_hora_atual = datetime.now()
                data_hora_formatada = data_hora_atual.strftime("%d-%m-%Y %H:%M:%S")
                
                info = f"Deposito de R${valor_transferencia} realizado."
                extrato = Extrato(data_hora_formatada, info)
            
                conta_encontrada.adicionar_extrato(extrato)
                
                data_hora_atual = datetime.now()
                data_hora_formatada = data_hora_atual.strftime("%d-%m-%Y %H:%M:%S")
                        
                h_info = f"Deposito feito na conta: {conta_destino}."
                h = Historico(data_hora_formatada,h_info)
                historico.append(h)
                
            else:
                print(f"Conta: {conta_destino} não encontrada.")
                
        elif opcao == 5:
            conta_destino = input("Número da conta destino: ")
            valor_transferencia = float(input("Valor a ser sacado: "))

            conta_encontrada = None

            for conta in contas:
                if str(conta.numero) == conta_destino:
                    conta_encontrada = conta
                    break

            if conta_encontrada:
                if conta_encontrada.saldo >= valor_transferencia:
                    conta_encontrada.saldo -= valor_transferencia
                    print(f"Saque de R$:{valor_transferencia:.2f} na conta {conta_encontrada.numero} realizado com sucesso.")
                    print(f"Saldo atual de R$:{conta_encontrada.saldo}")
                    
                    data_hora_atual = datetime.now()
                    data_hora_formatada = data_hora_atual.strftime("%d-%m-%Y %H:%M:%S")
                    
                    info = f"Saque de R${valor_transferencia} realizado."
                    extrato = Extrato(data_hora_formatada, info)
            
                    conta_encontrada.adicionar_extrato(extrato)
                    
                    data_hora_atual = datetime.now()
                    data_hora_formatada = data_hora_atual.strftime("%d-%m-%Y %H:%M:%S")
                        
                    h_info = f"Saque feito na conta: {conta_destino}."
                    h = Historico(data_hora_formatada,h_info)
                    historico.append(h)                    

                else:
                    print(f"Conta sem saldo suficiente!")
                    print(f"Saldo atual: R$:{conta_encontrada.saldo}")
            else:
                print(f"Conta: {conta_destino} não encontrada.")
                
        elif opcao == 6:
            conta_origem = input("Número da conta origem: ")
            conta_destino = input("Número da conta destino: ")
            valor_transferencia = float(input("Valor a ser transferido: "))

            conta_destino_encontrada = None
            conta_origem_encontrada = None

            for conta in contas:
                if str(conta.numero) == conta_origem:
                    conta_origem_encontrada = conta
                    break

            for conta in contas:
                if str(conta.numero) == conta_destino:
                    conta_destino_encontrada = conta
                    break

            if conta_origem_encontrada and conta_destino_encontrada:
                if conta_origem_encontrada.saldo >= valor_transferencia:
                    conta_origem_encontrada.saldo -= valor_transferencia
                    conta_destino_encontrada.saldo += valor_transferencia
                    print(f"Transferencia de R$:{valor_transferencia:.2f} da conta {conta_origem_encontrada.numero} para a conta {conta_destino_encontrada.numero} realizada com sucesso.")
                    print(f"Saldo atual da conta {conta_origem_encontrada.numero}: R$:{conta_origem_encontrada.saldo}")
                    print(f"Saldo atual da conta {conta_destino_encontrada.numero}: R$:{conta_destino_encontrada.saldo}")
                    
                    data_hora_atual = datetime.now()
                    data_hora_formatada = data_hora_atual.strftime("%d-%m-%Y %H:%M:%S")
                    
                    info_origem = f"Transferencia de R${valor_transferencia} realizada para a conta {conta_origem_encontrada.numero}."
                    extrato_origem = Extrato(data_hora_formatada, info_origem)
                    info_destino = f"Transferencia de R${valor_transferencia} recebida da conta {conta_destino_encontrada.numero}."
                    extrato_destino = Extrato(data_hora_formatada, info_destino)
                    
                    conta_origem_encontrada.adicionar_extrato(extrato_origem)
                    conta_destino_encontrada.adicionar_extrato(extrato_destino)
                    
                    data_hora_atual = datetime.now()
                    data_hora_formatada = data_hora_atual.strftime("%d-%m-%Y %H:%M:%S")
                        
                    h_info = f"Transferencia feita da conta {conta_origem_encontrada.numero} para conta {conta_destino_encontrada.numero}."
                    h = Historico(data_hora_formatada,h_info)
                    historico.append(h)   
                    
                else:
                    print(f"Conta origem sem saldo suficiente!")
                    print(f"Saldo atual: R$:{conta_origem_encontrada.saldo}")
            
            elif not conta_origem_encontrada and not conta_destino_encontrada:
                print(f"Conta origem: {conta_origem} não encontrada.")
                print(f"Conta destino: {conta_destino} não encontrada.")
                
            elif not conta_origem_encontrada:
                print(f"Conta origem: {conta_origem} não encontrada.")
            
            elif not conta_destino_encontrada:
                print(f"Conta destino: {conta_destino} não encontrada.")
                
        elif opcao == 7:
                extrato_conta = int(input("\nDigite o numero da conta desejada: "))

                for conta in contas:
                    if conta.numero == extrato_conta:
                        extrato_da_conta = conta.obter_extrato()
                        for extrato in extrato_da_conta:
                            print(f"Informacao: {extrato.informacao}, Data: {extrato.data}\n")

                data_hora_atual = datetime.now()
                data_hora_formatada = data_hora_atual.strftime("%d-%m-%Y %H:%M:%S")

                h_info = f"Extrato da conta {extrato_conta} acessado."
                h = Historico(data_hora_formatada, h_info)
                historico.append(h)

        
        elif opcao == 8:
            for his in historico:
                print(f"Evento: {his.informacao} - {his.data}\n")
                
    salvar_dados()
                        
if __name__ == "__main__":
    main()