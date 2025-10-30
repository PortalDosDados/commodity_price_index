import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Dados_commodities_mensal.csv')

print(df.info())

#print(df.head())

df['DATA'] = pd.to_datetime(df['CO_ANO'].astype(str) + '-' + df['CO_MES'].astype(str).str.zfill(2) + '-01')

# Substitui vírgula por ponto para conversão
df['INDICE'] = df['INDICE'].str.replace(',', '.', regex=False)

# Converte para float e arredonda
df['INDICE'] = df['INDICE'].astype(float).round(2)

# Formata de volta para string com vírgula
df['INDICE'] = df['INDICE'].map(lambda x: f"{x:.2f}".replace('.', ','))

print(df.head())