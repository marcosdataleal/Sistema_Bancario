class SistemaBancario:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.limite_saque_diario = 1000.0
        self.saques_hoje = 0.0
        self.limite_saques = 3
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if self.numero_saques >= self.limite_saques:
            print("Limite diário de saques atingido.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > self.limite_saque_diario - self.saques_hoje:
            print("Limite de saque diário excedido.")
        elif valor <= 0:
            print("O valor do saque deve ser positivo.")
        else:
            self.saldo -= valor
            self.saques_hoje += valor
            self.numero_saques += 1
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    def exibir_extrato(self):
        print("\n--- Extrato ---")
        if not self.extrato:
            print("Não foram realizadas operações.")
        else:
            for operacao in self.extrato:
                print(operacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("----------------\n")

def main():
    banco = SistemaBancario()

    while True:
        print("\n--- Menu ---")
        print("1. Depósito")
        print("2. Saque")
        print("3. Extrato")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: R$ "))
            banco.depositar(valor)
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: R$ "))
            banco.sacar(valor)
        elif opcao == "3":
            banco.exibir_extrato()
        elif opcao == "4":
            print("Obrigado por usar o sistema bancário!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
