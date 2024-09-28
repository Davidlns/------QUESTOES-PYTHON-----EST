#---------------------------------importa a biblioteca json e carrega o arquivo---------------------------------
import json

with open("dados.json", encoding='utf-8') as dd_json:
    dados = json.load(dd_json)

listavalores = []
listadias = []

#----------------------Cria duas listas para os dados do json valor e dia----------------------------------------
for i in dados:
    #print(i['valor'])
    listavalores.append(i['valor'])
    listadias.append(i['dia'])

#--------------------Identifica o menor valor sem contar os dias onde o faturamento foi 0 -----------------------
def menorf(l):
    a = 0
    menor = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000
    for i in l:
        if i < menor and i > 0:
            menor = i
            indice = a

        a = a + 1

    return indice
#-----------------------------------------------------------------------------------------------------------------

#---------------------------------------------------Identifica o maior valor--------------------------------------

def maiorf(l):
    a = 0
    maior = 0
    for i in l:
        if i > maior:
            maior = i
            indice = a

        a = a + 1

    return indice
#-----------------------------------------------------------------------------------------------------------------

#-----------------CALCULA A MEDIA DOS VALORES DESCONSIDERANDO OS DIAS QUE O FATURAMENTO FOI 0---------------------

def calcmedia(l):

    soma = 0
    dias = 0
    for i in l:
        if i > 0:
            soma = soma + i
            dias = dias + 1

    media = soma/dias
    dias = 0

    for i in l:
        if i < media and i > 0:
            dias = dias + 1

    return dias
 #---------------------------atribui o resultado das funções a variáveis e entrega o resultado----------------------
menor_faturamento = menorf(listavalores)
maior_faturamento = maiorf(listavalores)
dias_abaixo_media = calcmedia(listavalores)

print(f"""\nMenor faturamento foi no dia: {listadias[menor_faturamento]} com um valor de: {listavalores[menor_faturamento]}

Maior faturamento foi no dia {listadias[maior_faturamento]} com um valor de: {listavalores[maior_faturamento]}

O numero de dias no mês onde o faturamento foi menor que a média foi de: {dias_abaixo_media} dias""")


