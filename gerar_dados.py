# gerar_dados.py
# Script para gerar dados fictícios de vendas

import pandas as pd
import numpy as np

# Configurações iniciais
np.random.seed(42)
n = 500  # número de registros

# Gerando dados fictícios
clientes = [f'Cliente_{i}' for i in range(1, 51)]
produtos = ['Produto A', 'Produto B', 'Produto C', 'Produto D']
categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Casa']

dados = pd.DataFrame({
    'Cliente': np.random.choice(clientes, n),
    'Produto': np.random.choice(produtos, n),
    'Categoria': np.random.choice(categorias, n),
    'Quantidade': np.random.randint(1, 10, n),
    'Preço Unitário': np.round(np.random.uniform(10, 500), 2),
    'Data Venda': pd.date_range(start='2023-01-01', periods=n, freq='D')
})

# Calculando o valor total da venda
dados['Valor Total'] = dados['Quantidade'] * dados['Preço Unitário']

# Salvando em CSV
dados.to_csv('../dados/vendas.csv', index=False)
print("Dados de vendas gerados com sucesso!")
