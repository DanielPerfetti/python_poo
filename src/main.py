from frota import *
def operar_carro(carro : Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro.acelerar(v, t)

    print('Infos atuais do carro')
    print(carro)

if __name__ == "__main__":
    print('Cadastre o primeiro carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    n_tanque = float(input('Digite a quantidade de litros do tanque '))
    cm = float(input(' Consumo medio '))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, n_tanque, cm)

    print('Cadastre o segundo carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    n_tanque = float(input('Digite a quantidade de litros do tanque '))
    cm = float(input(' Consumo medio '))

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, n_tanque, cm)

    '''
    Controlando os carros até eles atingirigem 600 Km
    '''
    while carro1.odometro < 600 and carro2.odometro < 600 and (carro1.tanque > 0 or carro2.tanque > 0):
        try:
            op = 0
            while op not in (1, 2):
                op = int(input("Qual carro quer operar? [1-2]: "))

                if op == 1:
                    operar_carro(carro1)
                else:
                    operar_carro(carro2)

        except Exception as e:
            print("Erro!")
            print(e)


    carro1.desligar()
    print(carro1)
    carro2.desligar()
    print(carro2)

    if carro1.odometro > carro2.odometro:
        print("Carro 1 chegou primeiro ao destino")
    else:
        print("Carro 2 chegou primeiro ao destino")

#davi