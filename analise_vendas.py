# analise_vendas.py
# Script para análise de vendas utilizando Pandas, Matplotlib e Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações de visualização
plt.style.use('seaborn-whitegrid')
sns.set_palette('Set2')

# 1️⃣ Carregar os dados
dados = pd.read_csv('../dados/vendas.csv', parse_dates=['Data Venda'])

# 2️⃣ Limpeza e tratamento
# Verificando valores ausentes
print(dados.isnull().sum())

# Estatísticas básicas
print(dados.describe())

# 3️⃣ Análise exploratória
# Total de vendas por categoria
vendas_categoria = dados.groupby('Categoria')['Valor Total'].sum().sort_values(ascending=False)
print(vendas_categoria)

# Total de vendas por produto
vendas_produto = dados.groupby('Produto')['Valor Total'].sum().sort_values(ascending=False)
print(vendas_produto)

# Vendas ao longo do tempo
vendas_tempo = dados.groupby('Data Venda')['Valor Total'].sum()

# 4️⃣ Visualizações

# Gráfico 1: Total de vendas por categoria
plt.figure(figsize=(8,6))
sns.barplot(x=vendas_categoria.index, y=vendas_categoria.values)
plt.title('Total de Vendas por Categoria')
plt.ylabel('Valor Total (R$)')
plt.xlabel('Categoria')
plt.tight_layout()
plt.show()

# Gráfico 2: Total de vendas por produto
plt.figure(figsize=(8,6))
sns.barplot(x=vendas_produto.index, y=vendas_produto.values)
plt.title('Total de Vendas por Produto')
plt.ylabel('Valor Total (R$)')
plt.xlabel('Produto')
plt.tight_layout()
plt.show()

# Gráfico 3: Vendas ao longo do tempo
plt.figure(figsize=(12,6))
sns.lineplot(x=vendas_tempo.index, y=vendas_tempo.values)
plt.title('Evolução das Vendas ao Longo do Tempo')
plt.ylabel('Valor Total (R$)')
plt.xlabel('Data')
plt.tight_layout()
plt.show()

# Gráfico 4: Distribuição de valores das vendas
plt.figure(figsize=(8,6))
sns.histplot(dados['Valor Total'], bins=20, kde=True)
plt.title('Distribuição dos Valores de Vendas')
plt.xlabel('Valor Total (R$)')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()
