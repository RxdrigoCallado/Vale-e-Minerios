import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Lista de ativos
ativos = ['HG=F', 'VALE3.SA', 'BHP', 'TSI']

# Função para obter variações de ativos com base no número de dias
def obter_variacoes_com_dias(num_dias):
    data_inicio = datetime.now() - timedelta(days=num_dias)
    data_fim = datetime.now()
    variacoes = obter_variacoes_ativos(ativos, data_inicio, data_fim)
    salvar_variacoes(variacoes)

# Função para obter variações de ativos com base em datas
def obter_variacoes_com_datas(data_inicio, data_fim):
    data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")
    data_fim = datetime.strptime(data_fim, "%d/%m/%Y")
    variacoes = obter_variacoes_ativos(ativos, data_inicio, data_fim)
    salvar_variacoes(variacoes)

# Função para obter variações de ativos com base em datas ou número de dias
def obter_variacoes_ativos(tickers, data_inicio, data_fim):
    dados = yf.download(tickers, start=data_inicio, end=data_fim, interval='1d')
    variacoes = dados['Close'].pct_change().dropna()
    return variacoes

# Função para salvar os dados em um arquivo CSV
def salvar_variacoes(variacoes):
    df = pd.DataFrame({'Cobre': variacoes['HG=F'], 'VALE3': variacoes['VALE3.SA']})
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        df.to_csv(file_path, index=False)
        messagebox.showinfo("Sucesso", f"Dados salvos em {file_path}")

# Interface gráfica
window = tk.Tk()
window.title("Obter Variações de Ativos")
window.geometry("400x250")

# Label explicativo
label_explicativo = tk.Label(window, text="Escolha uma opção para obter variações:")
label_explicativo.pack()

# Function to open the date selection frame
def open_date_selection_frame(frame):
    frame.pack()
    if frame == numero_dias_frame:
        datas_especificas_frame.pack_forget()
    else:
        numero_dias_frame.pack_forget()

# Frame for "Número de Dias" option
numero_dias_frame = tk.Frame(window)

# Frame for "Datas Específicas" option
datas_especificas_frame = tk.Frame(window)

# Entry field for "Número de Dias"
label_dias = tk.Label(numero_dias_frame, text="Número de Dias:")
label_dias.pack()
entry_dias = tk.Entry(numero_dias_frame)
entry_dias.pack()

# Button to obtain variations with the number of days
button_dias = tk.Button(numero_dias_frame, text="Obter com Número de Dias", command=lambda: obter_variacoes_com_dias(int(entry_dias.get())))
button_dias.pack()

# Entry fields for "Datas Específicas"
data_inicio_label = tk.Label(datas_especificas_frame, text="Data de Início (DD/MM/AAAA):")
data_inicio_label.pack()
entry_data_inicio = tk.Entry(datas_especificas_frame)
entry_data_inicio.pack()

data_fim_label = tk.Label(datas_especificas_frame, text="Data de Fim (DD/MM/AAAA):")
data_fim_label.pack()
entry_data_fim = tk.Entry(datas_especificas_frame)
entry_data_fim.pack()

# Button to obtain variations with specific dates
obter_variacoes_datas_button = tk.Button(datas_especificas_frame, text="Obter Variações", command=lambda: obter_variacoes_com_datas(entry_data_inicio.get(), entry_data_fim.get()))
obter_variacoes_datas_button.pack()

# Button to choose the option of specific dates
button_datas = tk.Button(window, text="Datas Específicas", command=lambda: open_date_selection_frame(datas_especificas_frame))
button_datas.pack()

# Button to choose the option of number of days
button_dias = tk.Button(window, text="Número de Dias", command=lambda: open_date_selection_frame(numero_dias_frame))
button_dias.pack()

window.mainloop()
