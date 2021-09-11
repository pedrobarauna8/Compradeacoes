# FUTURO CODIGO QUE PEGA AS COTACOES AUTOMATICAMENTE
#from pandas_datareader import data as web
#import pandas as pd
#import matplotlib.pyplot as plt

#cotacao_bovespa = web.DataReader('^BVSP', data_source = 'yahoo', start = '01/01/2021', end = '12/01/2021')
#display(cotacao_bovespa)
 
ativo1 = float(input('Qual é o preço do primeiro ativo? '))
quantidade_ativo1 = float(input('Qual é a quantidade? '))
ativo2 = float(input('Qual é o preço do segundo ativo? '))
quantidade_ativo2 = float(input('Qual é a quantidade? '))
total_ativo1 = ativo1 * quantidade_ativo1
total_ativo2 = ativo2 * quantidade_ativo2
total = total_ativo1 + total_ativo2
print('Você precisará ter {} reais, para comprar {} reais do ativo 1 e {} do ativo 2'.format(total, total_ativo1, total_ativo2))
