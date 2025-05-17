# tupla com os meses
meses = ('reset', "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

num = int(input("Digite um número de 1 a 12: "))


if num > 13:
    print('seu burro')
else:
    print("O mês correspondente é:", meses[num])