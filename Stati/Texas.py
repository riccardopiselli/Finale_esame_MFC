import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import fft
import math
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import os




np.seterr(divide='ignore')




'''

Per il Texas il metodo è differente daglin altri stati....à
sono presenti più stazioni di monitoraggio e quiindi come prima cosa 
andiamo a creare nuovi csv solo con le singole stazzioni.

Secondo questo principio:



1415 Hinton Street   ---> Texas01
250 Rim Rd           ---> Texas02
800 S Son Marcial    ---> Texas03
7421 Park Place Blvd ---> Texas04
9525 1/2 Clinton Dr  ---> Texas05
4514 1/2 Durant St   ---> Texas06
4472 Mazanec Rd      ---> Texas07
3724 North Hills Dr  ---> Texas08



'''

mydf = pd.read_csv('Texas.csv')


correct_line_Texas01 = np.empty(0)
correct_line_Texas02 = np.empty(0)
correct_line_Texas03 = np.empty(0)
correct_line_Texas04 = np.empty(0)
correct_line_Texas05 = np.empty(0)
correct_line_Texas06 = np.empty(0)
correct_line_Texas07 = np.empty(0)
correct_line_Texas08 = np.empty(0)


N = len(mydf['Date Local'])
Address = mydf['Address']

for i in range(0,N-1):
    if Address[i] == '1415 Hinton Street':
       correct_line_Texas01 = np.append(correct_line_Texas01, i)
    
    elif Address[i] == '250 Rim Rd':
        correct_line_Texas02 = np.append(correct_line_Texas02, i)
    
    elif Address[i] == '800 S San Marcial Street' :
        correct_line_Texas03 = np.append(correct_line_Texas03, i)

  
    elif Address[i] == '7421 Park Place Blvd':
        correct_line_Texas04 = np.append(correct_line_Texas04, i)

    elif Address[i] == '9525 1/2 Clinton Dr':
        correct_line_Texas05 = np.append(correct_line_Texas05, i)

    elif Address[i] == '4514 1/2 Durant St':
        correct_line_Texas06 = np.append(correct_line_Texas06, i)
    
    elif Address[i] == '4472 Mazanec Rd':
        correct_line_Texas07 = np.append(correct_line_Texas07, i)
    
    elif Address[i] == '3724 North Hills Dr':
        correct_line_Texas08 = np.append(correct_line_Texas08, i)



df_Texas01 = mydf.iloc[correct_line_Texas01]
df_Texas02 = mydf.iloc[correct_line_Texas02]
df_Texas03 = mydf.iloc[correct_line_Texas03]
df_Texas04 = mydf.iloc[correct_line_Texas04]
df_Texas05 = mydf.iloc[correct_line_Texas05]
df_Texas06 = mydf.iloc[correct_line_Texas06]
df_Texas07 = mydf.iloc[correct_line_Texas07]
df_Texas08 = mydf.iloc[correct_line_Texas08]

'''



Salvo i risulatati dei miei dataframe in dei file csv... 



'''



df_Texas01.to_csv('Texas01.csv')
df_Texas02.to_csv('Texas02.csv')
df_Texas03.to_csv('Texas03.csv')
df_Texas04.to_csv('Texas04.csv')
df_Texas05.to_csv('Texas05.csv')
df_Texas06.to_csv('Texas06.csv')
df_Texas07.to_csv('Texas07.csv')
df_Texas08.to_csv('Texas08.csv')

