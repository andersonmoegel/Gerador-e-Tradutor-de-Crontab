import tkinter as tk
from tkinter import messagebox
import pyperclip

# Mapeamento de dias da semana
dias_semana = {
    "0": "domingo",
    "1": "segunda-feira",
    "2": "terça-feira",
    "3": "quarta-feira",
    "4": "quinta-feira",
    "5": "sexta-feira",
    "6": "sábado",
}

# Mapeamento de meses
meses_nomes = {
    "1": "Janeiro",
    "2": "Fevereiro",
    "3": "Março",
    "4": "Abril",
    "5": "Maio",
    "6": "Junho",
    "7": "Julho",
    "8": "Agosto",
    "9": "Setembro",
    "10": "Outubro",
    "11": "Novembro",
    "12": "Dezembro",
}

# Função para centralizar a janela
def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela - largura) // 2
    y = (altura_tela - altura) // 2
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

# Função para traduzir crontab
def traduzir_crontab(comando):
    partes = comando.split()
    if len(partes) != 5:
        return "Formato inválido! Um comando crontab deve ter 5 campos separados por espaços."

    minuto, hora, dia_mes, mes, dia_semana = partes

    if dia_semana != "*":
        dias = [v for k, v in dias_semana.items() if k in dia_semana.split(",")]
        dias = " e ".join(dias)
    else:
        dias = "todos os dias"

    traducao = f"Às {hora.zfill(2)}:{minuto.zfill(2)} {dias}."
    return traducao.strip()

# Função para gerar crontab
def gerar_crontab_interativo():
    hora = entrada_hora.get().strip() or "*"
    minuto = entrada_minuto.get().strip() or "*"

    dias_mes = [k for k, v in dias_mes_selecionados.items() if v.get()]
    dia_mes = ",".join(dias_mes) if dias_mes else "*"

    meses = [k for k, v in meses_selecionados.items() if v.get()]
    mes = ",".join(meses) if meses else "*"

    dias = [k for k, v in dias_selecionados.items() if v.get()]
    dia_semana = ",".join(dias) if dias else "*"

    comando = f"{minuto} {hora} {dia_mes} {mes} {dia_semana}"
    resultado_texto["text"] = f"Comando gerado: {comando}"
    botao_copiar["command"] = lambda: copiar_texto(comando)

# Função para copiar texto
def copiar_texto(texto):
    pyperclip.copy(texto)
    messagebox.showinfo("Copiado", "Texto copiado para a área de transferência!")

# Função para limpar campos
def limpar_campos():
    entrada_hora.delete(0, tk.END)
    entrada_minuto.delete(0, tk.END)
    for var in dias_selecionados.values():
        var.set(False)
    for var in meses_selecionados.values():
        var.set(False)
    for var in dias_mes_selecionados.values():
        var.set(False)
    resultado_texto["text"] = ""
    messagebox.showinfo("Limpar", "Todos os campos foram limpos!")

# Interface gráfica
def criar_interface():
    janela = tk.Tk()
    janela.title("Gerador e Tradutor de Crontab")
    largura, altura = 900, 750
    centralizar_janela(janela, largura, altura)
    janela.config(bg="#f0f0f0")

    # Título
    tk.Label(janela, text="Gerador e Tradutor de Crontab", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#5a5a5a").pack(pady=20)

    # Tradução
    tk.Label(janela, text="Tradução de Crontab:", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#5a5a5a").pack(pady=10)
    entrada_comando = tk.Entry(janela, font=("Arial", 12), width=40, bd=2, relief="solid", highlightthickness=2, highlightbackground="#007acc")
    entrada_comando.pack(pady=10)

    def traduzir():
        comando = entrada_comando.get().strip()
        if not comando:
            messagebox.showwarning("Aviso", "Insira um comando crontab para traduzir!")
            return
        try:
            resultado = traduzir_crontab(comando)
            resultado_texto["text"] = f"Tradução: {resultado}"
            botao_copiar["command"] = lambda: copiar_texto(resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    tk.Button(janela, text="Traduzir", font=("Arial", 12), bg="#007acc", fg="white", relief="flat", width=20, height=2, command=traduzir).pack(pady=10)

    # Geração
    tk.Label(janela, text="Geração de Crontab:", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#5a5a5a").pack(pady=10)

    # Hora e Minuto (lado a lado)
    linha_tempo = tk.Frame(janela, bg="#f0f0f0")
    linha_tempo.pack(pady=10)
    tk.Label(linha_tempo, text="Hora:", font=("Arial", 12), bg="#f0f0f0").pack(side="left", padx=10)
    global entrada_hora
    entrada_hora = tk.Entry(linha_tempo, font=("Arial", 12), width=10, bd=2, relief="solid", highlightthickness=2, highlightbackground="#007acc")
    entrada_hora.pack(side="left", padx=10)
    tk.Label(linha_tempo, text="Minuto:", font=("Arial", 12), bg="#f0f0f0").pack(side="left", padx=10)
    global entrada_minuto
    entrada_minuto = tk.Entry(linha_tempo, font=("Arial", 12), width=10, bd=2, relief="solid", highlightthickness=2, highlightbackground="#007acc")
    entrada_minuto.pack(side="left", padx=10)

    # Seções lado a lado
    geracao_frame = tk.Frame(janela, bg="#f0f0f0")
    geracao_frame.pack(pady=10)

    # Dias da Semana (4x3)
    dias_semana_frame = tk.Frame(geracao_frame, bg="#f0f0f0")
    dias_semana_frame.grid(row=0, column=0, padx=20)

    tk.Label(dias_semana_frame, text="Dias da Semana:", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#5a5a5a").grid(row=0, column=0, pady=5)

    global dias_selecionados
    dias_selecionados = {}
    for i, (k, v) in enumerate(dias_semana.items(), start=1):
        var = tk.BooleanVar()
        dias_selecionados[k] = var
        tk.Checkbutton(dias_semana_frame, text=v.capitalize(), variable=var, font=("Arial", 10), bg="#f0f0f0").grid(row=(i-1)//4+1, column=(i-1)%4, sticky="w", padx=5)

    # Meses (6x6)
    meses_frame = tk.Frame(geracao_frame, bg="#f0f0f0")
    meses_frame.grid(row=0, column=1, padx=20)

    tk.Label(meses_frame, text="Meses:", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#5a5a5a").grid(row=0, column=0, pady=5)

    global meses_selecionados
    meses_selecionados = {}
    for i, (k, v) in enumerate(meses_nomes.items(), start=1):
        var = tk.BooleanVar()
        meses_selecionados[k] = var
        tk.Checkbutton(meses_frame, text=v, variable=var, font=("Arial", 10), bg="#f0f0f0").grid(row=(i-1)//6+1, column=(i-1)%6, sticky="w", padx=5)

    # Dias do Mês (5x5)
    dias_mes_frame = tk.Frame(janela, bg="#f0f0f0")
    dias_mes_frame.pack(pady=20)

    tk.Label(dias_mes_frame, text="Dias do Mês:", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#5a5a5a").grid(row=0, column=0, pady=5)

    global dias_mes_selecionados
    dias_mes_selecionados = {}
    for i in range(1, 32):
        var = tk.BooleanVar()
        dias_mes_selecionados[str(i)] = var
        tk.Checkbutton(dias_mes_frame, text=str(i), variable=var, font=("Arial", 10), bg="#f0f0f0").grid(row=(i-1)//5+1, column=(i-1)%5, sticky="w", padx=5)

    # Botões
    btn_gerar = tk.Button(janela, text="Gerar Comando Crontab", font=("Arial", 12), bg="#28a745", fg="white", relief="flat", width=20, height=2, command=gerar_crontab_interativo)
    btn_gerar.pack(pady=10)

    btn_limpar = tk.Button(janela, text="Limpar", font=("Arial", 12), bg="#dc3545", fg="white", relief="flat", width=20, height=2, command=limpar_campos)
    btn_limpar.pack(pady=10)

    # Resultado
    global resultado_texto
    resultado_texto = tk.Label(janela, text="", font=("Arial", 12), wraplength=600, justify="left", bg="#f0f0f0", fg="#007acc")
    resultado_texto.pack(pady=10)

    global botao_copiar
    botao_copiar = tk.Button(janela, text="Copiar Resultado", font=("Arial", 12), bg="#007acc", fg="white", relief="flat", width=20, height=2)
    botao_copiar.pack(pady=10)

    janela.mainloop()

if __name__ == "__main__":
    criar_interface()
