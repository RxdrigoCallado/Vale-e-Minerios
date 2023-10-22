import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Lista de ativos
ativos = ['HG=F', 'VALE3.SA', 'BHP', 'TSI']

# Função para obter variações de ativos com base no número de dias
def obter_variacoes_ativos(tickers, num_dias):
    data_inicio = datetime.now() - timedelta(days=num_dias)
    data_fim = datetime.now()
    dados = yf.download(tickers, start=data_inicio, end=data_fim, interval='1d')
    variacoes = dados['Close'].pct_change().dropna()
    return variacoes

# Função para salvar os dados em um arquivo CSV
def salvar_dados_csv(df):
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        df.to_csv(file_path, index=False)
        messagebox.showinfo("Sucesso", f"Dados salvos em {file_path}")

# Interface gráfica
window = tk.Tk()
window.title("Obter Variações de Ativos")
window.geometry("300x200")

# Rótulo e entrada para o número de dias
dias_label = tk.Label(window, text="Número de dias para baixar:")
dias_label.pack()
dias_entry = tk.Entry(window)
dias_entry.pack()

# Botão para obter variações
def obter_variacoes():
    try:
        num_dias = int(dias_entry.get())
        variacoes = obter_variacoes_ativos(ativos, num_dias)

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
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido de dias.")

obter_variacoes_button = tk.Button(window, text="Obter Variações", command=obter_variacoes)
obter_variacoes_button.pack()

window.mainloop()
