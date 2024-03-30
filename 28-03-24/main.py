from platform import python_version
print('hello world', python_version())

from IPython.display import Image
Image('Workflow.png')

import os
import pandas as pd

# Obter o diretório atual do script
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Concatenar o diretório atual com o nome do arquivo
caminho_arquivo = os.path.join(diretorio_atual, 'pima-data.csv')

# Ler o arquivo CSV
df = pd.read_csv(caminho_arquivo)
print(df.tail(2))
print(df.isnull().values.any())# verifica se tem nulo

import matplotlib as mat
import matplotlib.pyplot as plt
import numpy as np
def plot_corr(df, size=10):
    corr = df.corr()
    fig, ax = plt.subplots(figsize = (size, size))
    ax.matshow(corr)
    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.yticks(range(len(corr.columns)), corr.columns)

plot_corr(df)
plt.show()#mostra o grafico