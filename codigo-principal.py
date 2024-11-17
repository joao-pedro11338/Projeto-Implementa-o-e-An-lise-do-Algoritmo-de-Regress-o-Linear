import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração de estilo de gráficos
sns.set(style="whitegrid")

# Carregar o dataset
file_path = 'caminho_para_o_arquivo.csv'  # Substitua pelo caminho do arquivo em seu computador
data = pd.read_csv(file_path)

# Função para converter valores com "k", "m", "b" e "%" em números
def convert_to_numeric(value):
    if isinstance(value, str):
        if 'k' in value:
            return float(value.replace('k', '').replace(',', '.')) * 1_000
        elif 'm' in value:
            return float(value.replace('m', '').replace(',', '.')) * 1_000_000
        elif 'b' in value:
            return float(value.replace('b', '').replace(',', '.')) * 1_000_000_000
        elif '%' in value:
            return float(value.replace('%', '').replace(',', '.')) / 100
    return value

# Converter as colunas relevantes
columns_to_convert = ['posts', 'followers', 'avg_likes', '60_day_eng_rate', 
                      'new_post_avg_like', 'total_likes']
for col in columns_to_convert:
    data[col] = data[col].apply(convert_to_numeric)

# Tratar valores ausentes na coluna "country"
data['country'] = data['country'].fillna('Unknown')  # Preencher nulos com 'Unknown'

# Análise Exploratória: Taxa de Engajamento por Nacionalidade
plt.figure(figsize=(12, 6))
sns.boxplot(x='country', y='60_day_eng_rate', data=data)
plt.xticks(rotation=45)
plt.title('Distribuição da Taxa de Engajamento por Nacionalidade')
plt.ylabel('Taxa de Engajamento (60 dias)')
plt.xlabel('Nacionalidade')
plt.show()

# Quantidade de influenciadores por nacionalidade (Top 10)
top_countries = data['country'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_countries.index, y=top_countries.values, palette="viridis")
plt.title('Top 10 Nacionalidades dos Influenciadores')
plt.ylabel('Quantidade de Influenciadores')
plt.xlabel('Nacionalidade')
plt.xticks(rotation=45)
plt.show()

# Correlação entre variáveis numéricas
plt.figure(figsize=(12, 8))
sns.heatmap(data.corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Mapa de Correlação das Variáveis')
plt.show()
