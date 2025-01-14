# Gerador e Tradutor de Crontab

Este projeto fornece uma interface gráfica de usuário (GUI) desenvolvida em Python com o uso da biblioteca `tkinter`. Ele permite gerar e traduzir expressões crontab para facilitar a configuração de tarefas agendadas em sistemas baseados em Unix.

## Funcionalidades

### Tradução de Crontab
- A ferramenta aceita um comando crontab no formato padrão (cinco campos separados por espaços).
- Após inserir o comando no campo de texto, clique no botão "Traduzir" para obter uma descrição amigável do agendamento.
- Exemplo de uso da função de tradução:
  ```python
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
  ```
- Este trecho de código divide o comando crontab em suas respectivas partes, mapeia os dias da semana e retorna uma tradução descritiva.

### Geração de Crontab
- Forneça as horas e minutos desejados para o agendamento.
- Selecione dias específicos da semana, do mês e meses do ano por meio de caixas de seleção.
- Clique em "Gerar Comando Crontab" para gerar um comando adequado.
- Exemplo de uso da função de geração:
  ```python
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
  ```
  - Essa função lê os valores das entradas e das seleções de caixas de verificação para construir o comando crontab correspondente.

### Copiar para Área de Transferência
- Tanto o comando crontab gerado quanto a tradução podem ser copiados para a área de transferência com um único clique.
- Exemplo de implementação:
  ```python
  def copiar_texto(texto):
      pyperclip.copy(texto)
      messagebox.showinfo("Copiado", "Texto copiado para a área de transferência!")
  ```

### Limpar Campos
- A funcionalidade de limpar campos redefine todas as entradas e desmarca as caixas de seleção para uma nova configuração.
- Exemplo:
  ```python
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
  ```

## Interface Gráfica
- A interface utiliza `tkinter` para criar um layout intuitivo com botões, caixas de seleção e campos de texto.
- A função `centralizar_janela` centraliza a janela principal:
  ```python
  def centralizar_janela(janela, largura, altura):
      largura_tela = janela.winfo_screenwidth()
      altura_tela = janela.winfo_screenheight()
      x = (largura_tela - largura) // 2
      y = (altura_tela - altura) // 2
      janela.geometry(f"{largura}x{altura}+{x}+{y}")
  ```

## Requisitos
- Python 3.x
- Bibliotecas:
  - `tkinter` (inclusa por padrão no Python)
  - `pyperclip` (para copiar textos para a área de transferência)

## Como Usar
1. Execute o script para abrir a interface.
2. Use o campo de texto para inserir comandos crontab e clique em "Traduzir".
3. Configure os campos de hora, minuto e selecione dias, meses ou dias do mês para gerar comandos.
4. Copie os resultados para a área de transferência com os botões fornecidos.

## Autor
Este projeto foi criado para simplificar o uso de agendamentos crontab, especialmente para novos usuários ou administradores de sistemas que desejam facilidade e precisão na configuração de cron jobs.

