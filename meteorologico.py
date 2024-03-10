meses = [
    "janeiro", 
    "fevereiro", 
    "março", 
    "abril", 
    "maio", 
    "junho",
    "julho", 
    "agosto", 
    "setembro", 
    "outubro", 
    "novembro", 
    "dezembro"
]

temp = []

for i in range(1, 13):
    mes = int(input("Mês ({}): ".format(i)))
    while mes < 1 or mes > 12:
        mes = int(input("Mês inválido. Digite novamente ({}): ".format(i)))
    temperatura = float(input("Temperatura máxima ({}): ".format(meses[i - 1])))
    while temperatura < -60 or temperatura > 50:
        temperatura = float(input("Temperatura inválida. Digite novamente ({}): ".format(meses[i - 1])))
    temp.append(temperatura)

media_maxima = sum(temp) / 12
meses_escaldantes = 0
mes_mais_escaldante = 0
mes_menos_quente = 0

for i in range(12):
    if temp[i] > 33:
        meses_escaldantes += 1
    if temp[i] > temp[mes_mais_escaldante]:
        mes_mais_escaldante = i
    if temp[i] < temp[mes_menos_quente]:
        mes_menos_quente = i

print("Temperatura média máxima anual: {:.2f} graus Celsius".format(media_maxima))
print("Quantidade de meses escaldantes: {}".format(meses_escaldantes))
print("Mês mais escaldante: {}".format(meses[mes_mais_escaldante]))
print("Mês menos quente: {}".format(meses[mes_menos_quente]))
