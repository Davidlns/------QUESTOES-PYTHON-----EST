#--------------------------------------------------------------------------------------------------------
import json

with open("fat_estados.json", encoding='utf-8') as estadosfat_json:
    dados = json.load(estadosfat_json)
lista_estados = []
lista_valores = []

#-----------------------------cria duas listas apartir do json com dados (estado, valor)-----------------
for i in dados:
    lista_estados.append(i['estado'])
    lista_valores.append(i['valor'])

#----------------soma todos os valores obtendo o equivalente a 100% do faturamento------------------------

def porcent100(lista):
    ftotal = 0
    for i in lista:
        ftotal = ftotal + i
    return float(ftotal)

#-----------------------Calcula a porc do faturamento da empresa com o estado------------------------------

def porcestado(valestado, porc100):
    porc_parcial = (valestado / porc100) * 100
    return porc_parcial

#------------------------printa todas as infos ativando as funções anteriores-------------------------------

print(f'\n 1 - O estado de {lista_estados[0]} equivale a {round(porcestado(lista_valores[0], porcent100(lista_valores)),2)}% do faturamento total da distribuidora')
print(f'\n 2 - O estado de {lista_estados[1]} equivale a {round(porcestado(lista_valores[1], porcent100(lista_valores)),2)}% do faturamento total da distribuidora')
print(f'\n 3 - O estado de {lista_estados[2]} equivale a {round(porcestado(lista_valores[2], porcent100(lista_valores)),2)}% do faturamento total da distribuidora')
print(f'\n 4 - O estado de {lista_estados[3]} equivale a {round(porcestado(lista_valores[3], porcent100(lista_valores)),2)}% do faturamento total da distribuidora')
print(f'\n 5 - {lista_estados[4]} equivale a {round(porcestado(lista_valores[4], porcent100(lista_valores)),2)}% do faturamento total da distribuidora')
print