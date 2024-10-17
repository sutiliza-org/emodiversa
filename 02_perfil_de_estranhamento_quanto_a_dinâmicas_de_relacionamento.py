# -*- coding: utf-8 -*-
"""02_Perfil_de_Estranhamento_quanto_a_Dinâmicas_de_Relacionamento.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xxnnKr46lHZEcGe6y7YpkuwF1olXXzcD
"""

from math import pi
import matplotlib.pyplot as plt
import pandas as pd

# Dados dos novos participantes e suas preferências
data = {
    'Participante': ['Helena', 'Isabela', 'João', 'Larissa', 'Marcos', 'Pedro', 'Raquel'],
    'Relação Aberta com Foco no Casual': [4, 3, 5, 2, 4, 3, 5],
    'Swing com Foco em Trocas Sexuais': [3, 4, 2, 5, 4, 5, 3],
    'Poliamor Não-Hierárquico com Baixa Interdependência': [5, 2, 4, 3, 5, 2, 4],
    'Relação Aberta com Conexões Emocionais Limitadas': [2, 5, 3, 4, 2, 4, 3],
    'Swing com Amizade e Conexão Social': [4, 3, 5, 2, 3, 5, 2],
    'Relação Aberta com Parceria Emocional Secundária': [3, 4, 5, 2, 4, 5, 3],
    'Poliamor Não-Hierárquico com Alta Interdependência': [5, 2, 3, 4, 5, 2, 4],
    'Swing com Conexões Emocionais': [2, 5, 4, 3, 2, 3, 5],
    'Swing Monogâmico': [4, 3, 5, 2, 3, 5, 2]
}

# Convertendo os dados para um DataFrame
df = pd.DataFrame(data)

# Definindo as categorias
categories = list(df.columns[1:])
N = len(categories)

# Configurações do gráfico polar
plt.figure(figsize=(10, 10), facecolor='black')
ax = plt.subplot(111, polar=True)

# Configurações dos eixos e ângulos
plt.xticks([n / float(N) * 2 * pi for n in range(N)], categories, color='white', fontsize=9)
ax.yaxis.grid(True, color='white', linestyle=':', linewidth=1)
ax.xaxis.grid(True, color='white', linestyle=':', linewidth=1)
ax.set_rscale('linear')
plt.yticks([1, 2, 3, 4, 5], ["Muito Pouco", "Pouco", "Regular", "Muito", "Bastante"], color="white", size=8)
ax.set_ylim(0, 5)

# Cores dos participantes (homens e mulheres)
male_colors = ['#4B0082', '#008000', '#0000FF']  # Roxo, Verde, Azul
female_colors = ['#FFFF00', '#FF4500', '#FF6347']  # Amarelo, Laranja, Vermelho

# Nome da pessoa central (agora uma mulher)
center_person = 'Larissa'

# Loop para plotar os dados de cada participante
for i, participant in enumerate(df['Participante']):
    if participant == center_person:
        color = 'white'  # Cor branca para a pessoa central (Larissa)
        linewidth = 4
    elif participant in ['João', 'Marcos', 'Pedro']:
        # Homens recebem as cores roxo, verde e azul
        color = male_colors[['João', 'Marcos', 'Pedro'].index(participant)]
        linewidth = 2
    elif participant in ['Helena', 'Isabela', 'Raquel']:
        # Mulheres recebem as cores amarelo, laranja e vermelho
        color = female_colors[['Helena', 'Isabela', 'Raquel'].index(participant)]
        linewidth = 2
    else:
        color = 'gray'  # Caso não seja definido, cor padrão cinza
        linewidth = 2

    # Obtendo os valores do participante
    values = df[df['Participante'] == participant].drop(columns='Participante').values.flatten().tolist()
    values += values[:1]  # Para fechar o gráfico

    # Calculando os ângulos para o gráfico polar
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]  # Para fechar o gráfico

    # Plota o gráfico polar para o participante
    plt.polar(angles, values, color=color, linewidth=linewidth, linestyle='solid')

# Título do gráfico
plt.title('Perfil de Estranhamento quanto a Dinâmicas de Relacionamento', color='white', fontsize=14)

# Legenda dos participantes
legend = plt.legend(df['Participante'].tolist(), loc='upper right', bbox_to_anchor=(1.2, 1.1), facecolor='black', labelcolor='white')
legend.get_title().set_color("white")

# Ajuste final no layout
plt.tight_layout()

# Exibe o gráfico
plt.show()