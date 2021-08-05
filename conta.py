class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo uma conta...{self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def extrato(self):
            print(f"Saldo de {self.__saldo} do titular {self.__titular}")

    def deposita(self, valor):
            self.__saldo = self.saldo + valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def tranfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @property
    def codigo_banco(self):
        return self.__codigo_banco

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}