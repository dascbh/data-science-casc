#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 20:32:42 2018

@author: Daniel Abraão
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

#%matplotlib inline

# carrega o dataset
df = pd.read_csv('https://s3-sa-east-1.amazonaws.com/danielabraao-01/quotes-AMD-01-to-15-OUT-2018.csv', index_col=0)

# imprime dataframe para validação
# print df

# declara variaveis principais  
date = "2018-10-10"
start_time = "09:30:00"
stop_time = "10:30:00"
ticker = "AMD"
metadata = "%s %s" % (date, ticker)

# indexa e prepara os dados para utilização
df_by_date = df.loc[date]
df_by_time = df
df_by_time['count'] = df_by_time.index
df_by_time = df_by_date.set_index('rtquotetime')
df_by_time = df_by_time.loc[start_time:stop_time]
df_by_time['rtquotetime'] = df_by_time.index


# plota primeiro grafico basico de evolução dos preços
plt.figure(figsize=(10, 7))
plt.title(metadata)
plt.plot(df_by_time['rtqlast'], markevery=100, label='quotes', linewidth=3) 

# plota gráficos de médias móveis simples - são dois, com janelas diferentes
window = 3
values = df_by_time['rtqlast']
weights = np.repeat(1.0, window) / window
smas = np.convolve(values,weights,'valid')
plt.plot(smas, color='Green', label='smas (3)')

# plota gráficos de médias móveis exponenciais
window = 4
weights = np.exp(np.linspace(-1., 0., window))
weights /= weights.sum()
emas =  np.convolve(values, weights, mode='full')[:len(values)]
emas[:window] = emas[window]
plt.plot(emas, color='Orange', label='emas (4)') 

plt.ylabel("preco")
plt.xlabel("linha do tempo")
plt.legend(loc='upper left')
plt.show()

# plota gráfico evolutivo do volume de transações
plt.figure(figsize=(10, 7))
plt.plot(df_by_time['rtqvolu'], color='Green', label='volume')    
plt.title(metadata)
plt.ylabel("volume")
plt.xlabel("linha do tempo")
plt.legend(loc='upper left')
plt.show()

# plota gráfico scatter comparando preço x volume e traça linha de tendência
plt.figure(figsize=(10, 7))
plt.title(metadata)
x = df_by_time['rtqvolu']
y = df_by_time['rtqlast']
plt.scatter(x=x, y=y, label='quotes')      

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--", label='tendencia')

plt.ylabel("preco")
plt.xlabel("volume")
plt.legend(loc='upper left')
plt.show()

# imprime descrição da série de últimos preços
df_by_time['rtqlast'].describe()