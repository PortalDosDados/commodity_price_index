import ssl
import pandas as pd

# Cria contexto SSL que ignora verificação
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://balanca.economia.gov.br/balanca/IPQ/arquivos/Dados_commodities_mensal.csv"
df = pd.read_csv(url, sep=';', encoding='UTF-8')

# Salvando localmente
df.to_csv("Dados_commodities_mensal.csv", index=False, encoding='utf-8')

print(df.head())
