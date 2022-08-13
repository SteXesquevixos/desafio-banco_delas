import numpy as np

class Cliente:
    def __init__(self, nome, telefone, renda_mensal, id_de_genero):
        self._nome = nome
        self._telefone = telefone
        self._renda_mensal = renda_mensal
        self._id_de_genero = id_de_genero

    def registrar_no_banco(self):
        BancoDelas.registrar_clientes(self._nome, self._telefone,
                                      self._renda_mensal, self._id_de_genero)


class BancoDelas(Cliente):
    BD_clientes = [["NOME", "TELEFONE", "RENDA MENSAL", "GÊNERO"]]

    def __init__(self, nome, telefone, renda_mensal, id_de_genero):
        super(BancoDelas, self).__init__(nome, telefone, renda_mensal, id_de_genero)

    @classmethod
    def registrar_clientes(cls, nome, telefone, renda_mensal, id_de_genero):
        cls.BD_clientes.append([nome, telefone, renda_mensal, id_de_genero])

    @classmethod
    def imprimir_BD(cls):
        print(f'{cls.BD_clientes[0][0]}\t\t'
              f'{cls.BD_clientes[0][1]}\t\t'
              f'{cls.BD_clientes[0][2]}\t\t'
              f'{cls.BD_clientes[0][3]}')
        for i in range(1, len(cls.BD_clientes)):
            print(f'{cls.BD_clientes[i][0]}\t'
                  f'{cls.BD_clientes[i][1]}\t\t'
                  f'{cls.BD_clientes[i][2]}\t\t\t'
                  f'{cls.BD_clientes[i][3]}')


class ContaCorrente:
    _saldo = 0
    limite_max = 0
    operacoes = list()

    def __init__(self, operacao):
        self.operacao = operacao

    @classmethod
    def saldo_por_cliente(cls):
        rendas_clientes = []
        for i in range(1, len(BancoDelas.BD_clientes)):
            rendas_clientes.append(BancoDelas.BD_clientes[i][2])
        cls._saldo += np.mean(rendas_clientes)
        cls.limite_max = 0

    @classmethod
    def saque(cls, operacao):
        if cls._saldo - operacao >= cls.limite_max:
            cls._saldo -= operacao
            ContaCorrente.registrar_operacoes(Tela(nome_cliente, tipo_operacao, valor_operacao).valor_operacao)
        elif cls._saldo - operacao < cls.limite_max:
            print("\nEsta operação não é permitida!\n"
                  "Você excedeu o valor máximo para saque.")

    @classmethod
    def deposito(cls, operacao):
        cls._saldo += operacao
        ContaCorrente.registrar_operacoes(Tela(nome_cliente, tipo_operacao, valor_operacao).valor_operacao)

    @classmethod
    def registrar_operacoes(cls, operacao):
        if Tela(nome_cliente, tipo_operacao, valor_operacao).tipo_operacao == 1:
            cls.operacoes.append(["Saque   ", operacao])
        elif Tela(nome_cliente, tipo_operacao, valor_operacao).tipo_operacao == 2:
            cls.operacoes.append(["Depósito", operacao])

    @classmethod
    def situacao_da_conta(cls):
        print(f'\n----Extrato----')
        for linha in range(len(cls.operacoes)):
            print(f'{cls.operacoes[linha][0]}\t{cls.operacoes[linha][1]}')
        print(f'Saldo disponível: {cls._saldo}')


class Mulher(ContaCorrente):
    _saldo = 0
    limite_max = 0
    operacoes = list()

    def __init__(self, operacao):
        self.operacao = operacao

    @classmethod
    def saldo_por_cliente(cls):
        rendas_clientes = []
        for i in range(1, len(BancoDelas.BD_clientes)):
            rendas_clientes.append(BancoDelas.BD_clientes[i][2])
        cls._saldo += np.mean(rendas_clientes)
        cls.limite_max -= cls._saldo

    @classmethod
    def saque(cls, operacao):
        if cls._saldo - operacao >= cls.limite_max:
            cls._saldo -= operacao
            Mulher.registrar_operacoes(Tela(nome_cliente, tipo_operacao, valor_operacao).valor_operacao)
        elif cls._saldo - operacao < cls.limite_max:
            print("\nEsta operação não é permitida!\n"
                  "Você excedeu o valor máximo para saque.\n")

    @classmethod
    def deposito(cls, operacao):
        cls._saldo += operacao
        Mulher.registrar_operacoes(Tela(nome_cliente, tipo_operacao, valor_operacao).valor_operacao)

    @classmethod
    def registrar_operacoes(cls, operacao):
        if Tela(nome_cliente, tipo_operacao, valor_operacao).tipo_operacao == 1:
            cls.operacoes.append(["Saque   ", operacao])
        elif Tela(nome_cliente, tipo_operacao, valor_operacao).tipo_operacao == 2:
            cls.operacoes.append(["Depósito", operacao])

    @classmethod
    def situacao_da_conta(cls):
        print(f'\n----Extrato----')
        for linha in range(len(cls.operacoes)):
            print(f'{cls.operacoes[linha][0]}\t{cls.operacoes[linha][1]}')
        print(f'Saldo disponível: {cls._saldo}')


class Homem(ContaCorrente):
    _saldo = 0
    limite_max = 0
    operacoes = list()

    def __init__(self, operacao):
        self.operacao = operacao

    @classmethod
    def saldo_por_cliente(cls):
        rendas_clientes = []
        for i in range(1, len(BancoDelas.BD_clientes)):
            rendas_clientes.append(BancoDelas.BD_clientes[i][2])
        cls._saldo += np.mean(rendas_clientes)
        cls.limite_max = 0

    @classmethod
    def saque(cls, operacao):
        if cls._saldo - operacao >= cls.limite_max:
            cls._saldo -= operacao
            Homem.registrar_operacoes(Tela(nome_cliente, tipo_operacao, valor_operacao).valor_operacao)
        elif cls._saldo - operacao < cls.limite_max:
            print("\nEsta operação não é permitida!\n"
                  "Você excedeu o valor máximo para saque.\n")

    @classmethod
    def deposito(cls, operacao):
        cls._saldo += operacao
        Homem.registrar_operacoes(Tela(nome_cliente, tipo_operacao, valor_operacao).valor_operacao)

    @classmethod
    def registrar_operacoes(cls, operacao):
        if Tela(nome_cliente, tipo_operacao, valor_operacao).tipo_operacao == 1:
            cls.operacoes.append(["Saque   ", operacao])
        elif Tela(nome_cliente, tipo_operacao, valor_operacao).tipo_operacao == 2:
            cls.operacoes.append(["Depósito", operacao])

    @classmethod
    def situacao_da_conta(cls):
        print(f'\n----Extrato----')
        for linha in range(len(cls.operacoes)):
            print(f'{cls.operacoes[linha][0]}\t{cls.operacoes[linha][1]}')
        print(f'Saldo disponível: {cls._saldo}')


class Tela:
    def __init__(self, nome_cliente, tipo_operacao, valor_operacao):
        self.nome_cliente = nome_cliente
        self.tipo_operacao = tipo_operacao
        self.valor_operacao = valor_operacao

    def tipos(self):
        for i in range(1, len(BancoDelas.BD_clientes) + 1):
            if self.nome_cliente == BancoDelas.BD_clientes[i][0]:
                if BancoDelas.BD_clientes[i][3] == "mulher" or BancoDelas.BD_clientes[i][3] == "mulher trans":
                    if self.tipo_operacao == 1:
                        Mulher.saque(self.valor_operacao)
                    elif self.tipo_operacao == 2:
                        Mulher.deposito(self.valor_operacao)
                    elif self.tipo_operacao == 3:
                        Mulher.situacao_da_conta()
                    break

                elif BancoDelas.BD_clientes[i][3] == "homem" or BancoDelas.BD_clientes[i][3] == "homem trans":
                    if self.tipo_operacao == 1:
                        Homem.saque(self.valor_operacao)
                    elif self.tipo_operacao == 2:
                        Homem.deposito(self.valor_operacao)
                    elif self.tipo_operacao == 3:
                        Homem.situacao_da_conta()
                    break


if __name__ == "__main__":
    # 1 - Registrar todos os titulares no banco e visualizar o saldo de cada um
    qnt_titulares = int(input(f'Número de clientes titulares: '))

    print("\n----Informe os dados dos titulares para fins de registro no Bando Delas----\n")

    for i in range(qnt_titulares):
        nome = str(input("Nome: "))
        telefone = str(input("Telefone: "))
        renda_mensal = int(input("Renda mensal: R$ "))
        id_de_genero = str(input("Gênero [mulher/homem (trans)]: "))
        print("\n")
        Cliente(nome, telefone, renda_mensal, id_de_genero).registrar_no_banco()

    BancoDelas.imprimir_BD()
    Mulher.saldo_por_cliente()
    Homem.saldo_por_cliente()

    # 2 - Verificar qual dos clientes pretende fazer uma operação
    nome_cliente = str(input("\nIdentificação [nome]: "))

    # 3 - Visualizar as opções disponíveis
    while True:
        print("\n----Opções disponíveis----")
        tipo_operacao = int(input(f'1 - Saque\n'
                                  f'2 - Depósito\n'
                                  f'3 - Saldo\n'
                                  f'4 - Sair\n'
                                  f'Tipo de operação: '))

        if tipo_operacao == 1 or tipo_operacao == 2:
            valor_operacao = int(input("Valor da operação: "))
            Tela(nome_cliente, tipo_operacao, valor_operacao).tipos()
        elif tipo_operacao == 3:
            Tela(nome_cliente, tipo_operacao, 0).tipos()
        else:
            break


