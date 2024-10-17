# -*- coding: utf-8 -*-
"""02-Comparação dos Perfis de Gestão Afetiva

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19zFCabM1sSBlPMulqi-1AMSEsRhZ3Jyo
"""

# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi
import io

# Dados em CSV (exemplo)
data_csv = """participante,tipo_relacionamento,responsabilidade_afetiva,independencia,coesao_social,comunicacao,compromisso,confiança,autocontrole,empatia,flexibilidade_cognitiva
Mateus,Poliamor Não-Hierárquico com Alta Interdependência,4.8,4.2,4.5,4.9,4.6,4.7,4.9,4.6,4.8
Lucas,Relação Aberta com Foco no Casual,4.1,4.5,4.2,4.3,4.7,4.0,4.4,4.3,4.2
João,Swing com Foco em Trocas Sexuais,3.4,4.0,3.6,3.8,4.1,4.2,4.4,3.9,4.0
Rafael,Relação Aberta com Envolvimento Emocional Limitado,4.5,4.1,4.3,4.5,4.2,4.1,4.3,4.5,4.1
Henrique,Swing Monogâmico,4.9,4.0,4.4,4.6,4.8,4.6,4.8,4.7,4.6
Ana,Poliamor Não-Hierárquico com Baixa Interdependência,4.3,4.3,4.1,4.4,4.3,4.2,4.4,4.3,4.2
Mariana,Swing com Amizade e Conexão Social,4.7,3.9,4.6,4.8,4.7,4.5,4.6,4.4,4.7
Juliana,Poliamor Não-Hierárquico com Alta Interdependência,4.9,4.8,4.9,5.0,4.9,4.8,4.9,4.9,4.8
Bianca,Swing com Conexões Emocionais,4.6,4.5,4.9,4.8,4.7,4.7,4.9,4.9,4.8
"""

# Carregando os dados
df = pd.read_csv(io.StringIO(data_csv))

# Definindo as variáveis para o gráfico
variaveis = ['responsabilidade_afetiva', 'independencia', 'coesao_social', 'comunicacao', 'compromisso', 'confiança', 'autocontrole', 'empatia', 'flexibilidade_cognitiva']
num_variaveis = len(variaveis)

# Função para gerar o gráfico de teia
def grafico_teia(df, participante_destaque):
    valores = df[variaveis].values.tolist()
    angulos = [n / float(num_variaveis) * 2 * pi for n in range(num_variaveis)]
    angulos += angulos[:1]

    plt.figure(figsize=(8, 8), facecolor='black')
    ax = plt.subplot(111, polar=True)
    ax.set_facecolor('black')

    # Cores: verde azulado ou azul para os homens, vermelho para as mulheres
    cores_azul_verde = ['#0077B6', '#009688', '#00B4D8', '#48CAE4', '#90E0EF']
    cores_vermelho = ['#FF4C4C', '#FF6F61', '#FF8C69']

    for i, participante in enumerate(df['participante']):
        valores_participante = valores[i]
        valores_participante += valores_participante[:1]

        # Homem destacado em amarelo
        if participante == participante_destaque:
            ax.plot(angulos, valores_participante, linewidth=2, linestyle='solid', label=participante, color='yellow')
            ax.fill(angulos, valores_participante, color='yellow', alpha=0.3)
        # Mulheres em vermelho
        elif participante in ['Ana', 'Mariana', 'Juliana', 'Bianca']:
            cor_vermelho = cores_vermelho[i % len(cores_vermelho)]
            ax.plot(angulos, valores_participante, linewidth=1, linestyle='solid', label=participante, color=cor_vermelho, alpha=0.5)
        # Homens em azul ou verde
        else:
            cor_homem = cores_azul_verde[i % len(cores_azul_verde)]
            ax.plot(angulos, valores_participante, linewidth=1, linestyle='solid', label=participante, color=cor_homem, alpha=0.5)

    plt.xticks(angulos[:-1], variaveis, color='white', size=10)
    ax.tick_params(colors='white')
    ax.yaxis.set_tick_params(labelsize=8)
    ax.set_rlabel_position(0)

    plt.title('Comparação dos Perfis de Gestão Afetiva', size=16, color='white', y=1.08)
    plt.tight_layout()
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
    plt.show()

# Gerando o gráfico com Mateus em destaque
grafico_teia(df, 'Mateus')

