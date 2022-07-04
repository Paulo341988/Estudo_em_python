print ("\n======   Bem vindo ao caixa eletroico   =======\n\nNotas Disponiveis R$ 1, 5, 10, 20, 50, 100")

saque = int(input(" \nvalor maximo para saque 600,00\nDigite o Valor do saque:"))


if 10 <= saque <= 600:
    notas_cem = saque // 100
    saque = saque % 100

    notas_cinquenta = saque // 50
    saque = saque % 50

    notas_dez = saque // 10
    saque = saque % 10

    notas_cinco = saque // 5
    saque = saque % 5

    notas_um = saque // 1


    if 10 <= 600:
        print("\nNotas a serem sacadas\n") 
    if notas_cem > 0:
        print(notas_cem, "notas de R$ 100,00")
    if notas_cinquenta > 0:
        print(notas_cinquenta, "notas de R$ 50,00")
    if notas_dez > 0:
        print(notas_dez, "notas de R$ 10,00")
    if notas_cinco > 0:
        print(notas_cinco, "notas de R$ 5,00")
    if notas_um > 0:
        print(notas_um, "notas de R$ 1,00")
            
else:
    print("\nNao é possivel fazer o saque limite superior a R$600,00")

input()
