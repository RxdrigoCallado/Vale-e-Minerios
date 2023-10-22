import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Lista de ativos
ativos = ['HG=F', 'VALE3.SA', 'BHP', 'TSI']

# Função para obter variações de ativos com base no número de dias e datas
def obter_variacoes_ativos(tickers, num_dias, data_inicio, data_fim):
    dados = yf.download(tickers, start=data_inicio, end=data_fim, interval='1d')
    variacoes = dados['Close'].pct_change().dropna()
    return variacoes

# Função para salvar os dados em um arquivo CSV
def salvar_dados_csv(df):
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        df.to_csv(file_path, index=False)
        messagebox.showinfo("Sucesso", f"Dados salvos em {file_path}")

# Função para abrir a janela de datas
def abrir_janela_datas():
    # Crie uma nova janela para inserir datas
    janela_datas = tk.Tk()
    janela_datas.title("Selecionar Datas")
    janela_datas.geometry("300x200")

    # Rótulo e entrada para a data de início
    data_inicio_label = tk.Label(janela_datas, text="Data de Início (DD/MM/AAAA):")
    data_inicio_label.pack()
    entry_data_inicio = tk.Entry(janela_datas)
    entry_data_inicio.pack()

    # Rótulo e entrada para a data de fim
    data_fim_label = tk.Label(janela_datas, text="Data de Fim (DD/MM/AAAA):")
    data_fim_label.pack()
    entry_data_fim = tk.Entry(janela_datas)
    entry_data_fim.pack()

    # Botão para obter variações com datas
    obter_variacoes_datas_button = tk.Button(janela_datas, text="Obter Variações", command=lambda: obter_variacoes_com_datas(entry_data_inicio.get(), entry_data_fim.get()))
    obter_variacoes_datas_button.pack()

    # Feche a janela após o uso
    janela_datas.mainloop()

# Função para obter variações
def obter_variacoes():
    num_dias = int(entry_dias.get())
    data_inicio = datetime.now() - timedelta(days=num_dias)
    data_fim = datetime.now()
    variacoes = obter_variacoes_ativos(ativos, num_dias, data_inicio, data_fim)

    cobre_variacoes = variacoes['HG=F']
    niquel_variacoes = variacoes['BHP']
    ferro_variacoes = variacoes['TSI']

    peso_cobre = 0.415
    peso_niquel = 0.21
    peso_ferro = 0.375
    media_ponderada = (
        peso_cobre * cobre_variacoes +
        peso_niquel * niquel_variacoes +
        peso_ferro * ferro_variacoes
    )

    vale_variacoes = variacoes['VALE3.SA']

    dados_x = cobre_variacoes
    dados_y = vale_variacoes
    dados_x_media = media_ponderada
    dados_y_media = vale_variacoes

    df = pd.DataFrame({'Cobre': dados_x, 'VALE3': dados_y, 'Média Ponderada': dados_x_media, 'Variação VALE3': dados_y_media})

    salvar_dados_csv(df)

# Interface gráfica
window = tk.Tk()
window.title("Obter Variações de Ativos")
window.geometry("300x200")

# Rótulo e entrada para o número de dias
dias_label = tk.Label(window, text="Baixar Dados dos Ultimos Dias:")
dias_label.pack()
entry_dias = tk.Entry(window)
entry_dias.pack()

# Botão para obter variações
obter_variacoes_button = tk.Button(window, text="Obter Variações", command=obter_variacoes)
obter_variacoes_button.pack()

# Botão para abrir a janela de datas
datas_button = tk.Button(window, text="Selecionar Datas", command=abrir_janela_datas)
datas_button.pack()

window.mainloop()
