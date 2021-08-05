class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def __verificar_mes(self):
        return self.__mes <= 12 and self.__mes >= 1

    def __verificar_dia(self):
        if(not self.__verificar_mes()):
            return self.__dia <= 31
        else:
            dias_max_do_mes = (31, 29, 31, 30, 31, 30, 31, 31, 30, 30, 30, 31)
            mes_escolhido = self.__mes - 1
            y = dias_max_do_mes[mes_escolhido]
            return self.__dia <= y and self.__dia >= 1

    def formatar(self):
        if(self.__verificar_dia() and self.__verificar_mes()):
            print(f"{self.__dia}/{self.__mes}/{self.__ano}")
        elif(not self.__verificar_dia() and self.__verificar_mes()):
            print("dia inválido")
        elif(self.__verificar_dia() and not self.__verificar_mes()):
            print("mês inválido")
        elif( not self.__verificar_dia() and not self.__verificar_mes()):
            print("dia e mês inválidos")