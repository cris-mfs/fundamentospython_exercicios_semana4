#Exercício Ficha de Trabalho semana 4 - Cristiano Silva

import pandas as pd

def ler_dados_excel(caminho_do_ficheiro):
    # Lê os dados
    return pd.read_excel(caminho_do_ficheiro)

def filtra_dados_por_paiís(dados, nome_país):
    # Filtro os dados pelo noem do país
    return dados[dados["Country Name"]==nome_país]

def calcular_variação_percentual(valor_inicial, valor_final):
    # Calcula a variação percentual entre dois valores
    return (valor_final-valor_inicial)/valor_inicial * 100

dados = ler_dados_excel("P_Data_Extract_From_World_Development_Indicators.xlsx")
dados = dados[["Country Name", "1990 [YR1990]", "2000 [YR2000]"]] # refinação de dados

dados_portugal = filtra_dados_por_paiís(dados, "Portugal")

consumo_inicial = dados_portugal["1990 [YR1990]"].values[0]
consumo_final = dados_portugal["2000 [YR2000]"].values[0]
variacao = calcular_variação_percentual(consumo_inicial, consumo_final)

#Gráfico de Barras

import matplotlib.pyplot as plt

categorias = ["Ano 1990", "Ano 2000"]
valores = [consumo_inicial,consumo_final]

plt.bar(categorias, valores, color="blue")
plt.xlabel("País em análise: Portugal")
plt.ylabel("Consumo de energia [kWh]")
titulo = f"Variação de consumo de energia elétrica em Portugal entre 1990 e 2000.\n Variação percentual no consumo entre 1990 e 2000 foi de {variacao:.2f}%"
plt.title(titulo)
plt.show()