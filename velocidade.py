# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 23:09:06 2022

@author: jdebr
"""
import math
'''calculo de velocidades relativas com base na diferença de anomalia de geopotencial - Método dinâmico'''

'''parametro de coriolis'''
coriolis=9.7*10**(-5)

'''calculando velocidades relativas'''
def vel_geo(l,a,b,coriolis):
    return (1/(l*coriolis))*(b-a)

'''anomalias de geopotencial'''

estacao_a=[6.638
,6.273
,5.935
,5.620
,5.315
,4.755
,4.300
,3.470
,2.820
,1.780
,0.880
,0]
    
estacao_b=[7.894
,7.596
,7.298
,7.000
,6.700
,6.090
,5.480
,4.310
,3.330
,1.930
,0.900
,0]


'''considerando a distancia de 50 km entre estações'''
vel_relativa_50=[]
for i in range(len(estacao_a)):
    vel_relativa_50.append(round(vel_geo(50*10**3,estacao_a[i],estacao_b[i],coriolis),2))
    
'''considerando a distância de 25km entre estações'''
vel_relativa_25=[]
for i in range(len(estacao_a)):
    vel_relativa_25.append(round(vel_geo(25*10**3,estacao_a[i],estacao_b[i],coriolis),2))
    
'''considerando a distância de 100 km entre estações'''
vel_relativa_100=[]
for i in range(len(estacao_a)):
    vel_relativa_100.append(round(vel_geo(100*10**3,estacao_a[i],estacao_b[i],coriolis),2))