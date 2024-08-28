class Carro:
    modelo : str
    marca : str
    cor : str
    __odometro = 0.0
    __tanque = 0.0
    consumo_medio : float
    __motor_on = False

    def __init__(self, modelo : str, marca : str, cor : str,
                       __odometro : float, __motor : bool, __tanque : float, consumo_medio : float):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.__odometro = __odometro
        self.__tanque = __tanque
        self.consumo_medio = consumo_medio
        self.__motor_on = __motor

    def ligar(self):
        if not self.__motor_on and self.__tanque > 0:
            self.__motor_on = True
        else:
            raise Exception("Erro: motor já ligado ou tanque vazio!")

    def acelerar(self, velocidade : float, tempo : float):
        if self.__motor_on and self.__tanque > 0:
            km = velocidade * tempo
            litros = km/self.consumo_medio
            if self.__tanque >= litros:
                self.__tanque -= litros
            else:
                km = litros * self.consumo_medio
                self.__tanque = 0
                self.desligar()
            self.__odometro += km
        else:
            raise Exception("Erro: Não é possível acelerar! motor desligado ou sem combustivel!")

    def desligar(self):
        if self.__motor_on:
            self.__motor_on = False
        else:
            raise Exception("Erro: motor já desligado!")

    def __str__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.__odometro} Km, '
                f'motor {self.__motor_on}, consumo {self.consumo_medio}, km/l tanque {self.__tanque} L')
        return info

    def get_odometro(self):
        return self.__odometro

    def get_tanque(self):
        return self.__tanque


#davi




