import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from scipy.optimize import minimize_scalar
import sympy as sp

# Variável global para armazenar o canvas
canvas = None

def plotar_curva(intervalo, funcao):
    x = np.linspace(intervalo[0], intervalo[1], 100)
    y = funcao(x)

    plt.figure(figsize=(5, 4))
    plt.plot(x, y, label='Função Objetivo')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Curva da Função Objetivo')
    plt.grid(True)
    plt.legend()

    return plt

def calcular_ponto_minimo():
    valor_inicio = entry_inicio.get()
    valor_fim = entry_fim.get()
    expressao_funcao = entry_funcao.get()

    # Verifica se os campos de entrada contêm valores válidos
    if not valor_inicio.isdigit() or not valor_fim.isdigit():
        # Se um dos campos não for um número, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Por favor, insira valores numéricos nos campos de início e fim do intervalo.")
        return

    try:
        # Tenta converter os valores para float
        inicio = float(valor_inicio)
        fim = float(valor_fim)
    except ValueError:
        # Se a conversão falhar, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Valores inválidos. Certifique-se de inserir números válidos.")
        return

    try:
        # Tenta converter a expressão da função para uma função Sympy
        x = sp.symbols('x')
        funcao_objetivo = sp.lambdify(x, sp.sympify(expressao_funcao), 'numpy')
    except (sp.SympifyError, TypeError):
        # Se a conversão falhar, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Função inválida. Certifique-se de inserir uma expressão matemática válida.")
        return

    # Utiliza a função minimize_scalar do SciPy para encontrar o mínimo
    resultado = minimize_scalar(funcao_objetivo, bounds=(inicio, fim), method='bounded')

    # Exibe o ponto mínimo
    messagebox.showinfo("Resultado", f'O ponto mínimo é: x = {resultado.x:.2f}, y = {resultado.fun:.2f}')

# ...

def atualizar_grafico():
    global canvas

    expressao_funcao = entry_funcao.get()

    valor_inicio = entry_inicio.get()
    valor_fim = entry_fim.get()

    # Verifica se os campos de entrada contêm valores válidos
    if not valor_inicio.replace('.', '').isdigit() or not valor_fim.replace('.', '').isdigit():
        # Se um dos campos não for um número, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Por favor, insira valores numéricos nos campos de início e fim do intervalo.")
        return

    try:
        # Tenta converter os valores para float
        inicio = float(valor_inicio)
        fim = float(valor_fim)
    except ValueError:
        # Se a conversão falhar, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Valores inválidos. Certifique-se de inserir números válidos.")
        return

    intervalo = (inicio, fim)

    try:
        # Tenta converter a expressão da função para uma função Sympy
        x = sp.symbols('x')
        funcao_objetivo = sp.lambdify(x, sp.sympify(expressao_funcao), 'numpy')
    except (sp.SympifyError, TypeError):
        # Se a conversão falhar, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Função inválida. Certifique-se de inserir uma expressão matemática válida.")
        return

    # Criar array de valores de x
    x_vals = np.linspace(inicio, fim, 100)

    # Recriar o gráfico
    plt = plotar_curva(intervalo, funcao_objetivo)

    # Limpar o canvas antigo, se existir
    if canvas:
        canvas.get_tk_widget().destroy()

    # Adicionar o novo gráfico ao canvas
    canvas = FigureCanvasTkAgg(plt.gcf(), master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)




# Função para avaliar a expressão da função nos pontos do array
def avaliar_funcao(x):

    y_vals = funcao_objetivo(x)

    return y_vals



# Encontrar o Valor Máximo ou Mínimo:
# Use np.max ou np.min para encontrar o valor máximo ou mínimo da função.

def calcular_ponto_minimo():
    valor_inicio = entry_inicio.get()
    valor_fim = entry_fim.get()
    expressao_funcao = entry_funcao.get()

    # Verifica se os campos de entrada contêm valores válidos
    if not valor_inicio.isdigit() or not valor_fim.isdigit():
        # Se um dos campos não for um número, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Por favor, insira valores numéricos nos campos de início e fim do intervalo.")
        return

    try:
        # Tenta converter os valores para float
        inicio = float(valor_inicio)
        fim = float(valor_fim)
    except ValueError:
        # Se a conversão falhar, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Valores inválidos. Certifique-se de inserir números válidos.")
        return

    try:
        # Tenta converter a expressão da função para uma função Sympy
        x = sp.symbols('x')
        funcao_objetivo = sp.lambdify(x, sp.sympify(expressao_funcao), 'numpy')
    except (sp.SympifyError, TypeError):
        # Se a conversão falhar, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Função inválida. Certifique-se de inserir uma expressão matemática válida.")
        return

    # Utiliza a função minimize_scalar do SciPy para encontrar o mínimo
    resultado = minimize_scalar(funcao_objetivo, bounds=(inicio, fim), method='bounded')

    # Exibe o ponto mínimo
    messagebox.showinfo("Resultado", f'O ponto mínimo é: x = {resultado.x:.2f}, y = {resultado.fun:.2f}')

def calcular_ponto_maximo():
    valor_inicio = entry_inicio.get()
    valor_fim = entry_fim.get()
    expressao_funcao = entry_funcao.get()

    # Verifica se os campos de entrada contêm valores válidos
    if not valor_inicio.isdigit() or not valor_fim.isdigit():
        # Se um dos campos não for um número, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Por favor, insira valores numéricos nos campos de início e fim do intervalo.")
        return

    try:
        # Tenta converter os valores para float
        inicio = float(valor_inicio)
        fim = float(valor_fim)
    except ValueError:
        # Se a conversão falhar, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Valores inválidos. Certifique-se de inserir números válidos.")
        return

    try:
        # Tenta converter a expressão da função para uma função Sympy
        x = sp.symbols('x')
        funcao_objetivo = sp.lambdify(x, sp.sympify(expressao_funcao), 'numpy')
    except (sp.SympifyError, TypeError):
        # Se a conversão falhar, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Função inválida. Certifique-se de inserir uma expressão matemática válida.")
        return

    # Utiliza a função minimize_scalar do SciPy para encontrar o máximo
    resultado = minimize_scalar(lambda x: -funcao_objetivo(x), bounds=(inicio, fim), method='bounded')

    # Exibe o ponto máximo
    messagebox.showinfo("Resultado", f'O ponto máximo é: x = {resultado.x:.2f}, y = {-resultado.fun:.2f}')

# Encontrar a Média e o Desvio Padrão:
# Use np.mean e np.std para calcular a média e o desvio padrão.

def media():
    valor_inicio = entry_inicio.get()
    valor_fim = entry_fim.get()
    expressao_funcao = entry_funcao.get()

    # Verifica se os campos de entrada contêm valores válidos
    if not valor_inicio.isdigit() or not valor_fim.isdigit():
        # Se um dos campos não for um número, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Por favor, insira valores numéricos nos campos de início e fim do intervalo.")
        return

    try:
        # Tenta converter os valores para float
        inicio = float(valor_inicio)
        fim = float(valor_fim)
    except ValueError:
        # Se a conversão falhar, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Valores inválidos. Certifique-se de inserir números válidos.")
        return

    try:
        # Tenta converter a expressão da função para uma função Sympy
        x = sp.symbols('x')
        funcao_objetivo = sp.lambdify(x, sp.sympify(expressao_funcao), 'numpy')
    except (sp.SympifyError, TypeError):
        # Se a conversão falhar, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Função inválida. Certifique-se de inserir uma expressão matemática válida.")
        return

    # Avaliar a função nos pontos do intervalo
    x_vals = np.linspace(inicio, fim, 100)
    y_vals = funcao_objetivo(x_vals)

    # Calcular a média da função
    media = np.mean(y_vals)
    
    # Exibir o resultado
    messagebox.showinfo("Resultado", f'A média da função é: {float(media):.2f}')


def desvio_padrao():
    valor_inicio = entry_inicio.get()
    valor_fim = entry_fim.get()
    expressao_funcao = entry_funcao.get()

    # Verifica se os campos de entrada contêm valores válidos
    if not valor_inicio.isdigit() or not valor_fim.isdigit():
        # Se um dos campos não for um número, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Por favor, insira valores numéricos nos campos de início e fim do intervalo.")
        return

    try:
        # Tenta converter os valores para float
        inicio = float(valor_inicio)
        fim = float(valor_fim)
    except ValueError:
        # Se a conversão falhar, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Valores inválidos. Certifique-se de inserir números válidos.")
        return

    try:
        # Tenta converter a expressão da função para uma função Sympy
        x = sp.symbols('x')
        funcao_objetivo = sp.lambdify(x, sp.sympify(expressao_funcao), 'numpy')
    except (sp.SympifyError, TypeError):
        # Se a conversão falhar, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Função inválida. Certifique-se de inserir uma expressão matemática válida.")
        return
    
    # Avaliar a função nos pontos do intervalo
    x_vals = np.linspace(inicio, fim, 100)
    y_vals = funcao_objetivo(x_vals)
    desvio_padrao = np.std(y_vals)
    messagebox.showinfo("Resultado", f'O desvio padrão da função é de {float(desvio_padrao):.2f}')

# Operações Elementares/Vetoriais:
# Realize operações elementares nos valores da função.


# Encontrar Zeros da Função:
# Use np.roots para encontrar as raízes (zeros) da função.

def raizes():
    expressao_funcao = entry_funcao.get()

    try:
        # Tenta converter a expressão da função para uma função Sympy
        coeficientes = sp.Poly(sp.sympify(expressao_funcao)).all_coeffs()

        # Encontra todas as raízes da função
        todas_raizes = np.roots(coeficientes)

        # Filtra apenas as raízes reais
        raizes_reais = [raiz.real for raiz in todas_raizes if raiz.imag == 0]

        messagebox.showinfo("Resultado", f'As raízes reais da função são: x = {raizes_reais}')
    except sp.SympifyError as e:
        # Se a conversão falhar, mostra uma mensagem de aviso com o erro específico
        messagebox.showwarning("Aviso", f"Erro na conversão da função: {e}")


# Integração Numérica:
# Use np.trapz ou np.simps para realizar integração numérica da função.

def area_integracao():
    valor_inicio = entry_inicio.get()
    valor_fim = entry_fim.get()
    expressao_funcao = entry_funcao.get()

    # Verifica se os campos de entrada contêm valores válidos
    if not valor_inicio.isdigit() or not valor_fim.isdigit():
        # Se um dos campos não for um número, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Por favor, insira valores numéricos nos campos de início e fim do intervalo.")
        return

    try:
        # Tenta converter os valores para float
        inicio = float(valor_inicio)
        fim = float(valor_fim)
    except ValueError:
        # Se a conversão falhar, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Valores inválidos. Certifique-se de inserir números válidos.")
        return

    try:
        # Tenta converter a expressão da função para uma função Sympy
        x = sp.symbols('x')
        funcao_objetivo = sp.lambdify(x, sp.sympify(expressao_funcao), 'numpy')
    except (sp.SympifyError, TypeError):
        # Se a conversão falhar, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Função inválida. Certifique-se de inserir uma expressão matemática válida.")
        return
    
    # Avaliar a função nos pontos do intervalo
    x_vals = np.linspace(inicio, fim, 100)
    y_vals = funcao_objetivo(x_vals)
    area_sob_a_curva = np.trapz(y_vals, x_vals)
    messagebox.showinfo("Resultado", f'A área sob a curva da função é: {area_sob_a_curva:.2f}')


def derivada():
    expressao_funcao = entry_funcao.get()
    ponto = entry_ponto.get()

    # Verifica se os campos de entrada contêm valores válidos
    if not ponto.replace(".", "").isdigit():  # Permitir ponto decimal
        # Se o ponto não for um número, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Por favor, insira o valor numérico no campo do ponto da derivada.")
        return

    try:
        # Tenta converter os valores para float
        ponto = float(ponto)
    except ValueError:
        # Se a conversão falhar, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Valor inválido. Certifique-se de inserir um número válido.")
        return
    
    try:
        # Tenta converter a expressão da função para uma função Sympy
        x = sp.symbols('x')
        funcao_objetivo = sp.sympify(expressao_funcao)
        derivada = sp.diff(funcao_objetivo, x)
        valor_derivada = derivada.subs(x, ponto)
        messagebox.showinfo("Resultado", f'A derivada em x={ponto} é: {valor_derivada}')
    except (sp.SympifyError, TypeError):
        # Se a conversão falhar, mostra uma mensagem de aviso
        messagebox.showwarning("Aviso", "Função inválida. Certifique-se de inserir uma expressão matemática válida.")
        return


# Estilo para a janela principal
app = tk.Tk()
app.title("Visualizador de Função Objetivo")

# Frame para entrada de dados
frame_entrada = ttk.Frame(app)
frame_entrada.pack(side=tk.TOP, padx=10, pady=10)

label_function = ttk.Label(frame_entrada, text="Função: ")
label_function.grid(row=0, column=0, padx=5, pady=5)

entry_funcao = ttk.Entry(frame_entrada)
entry_funcao.grid(row=0, column=1, padx=5, pady=5)
entry_funcao.insert(0, "-x**3 - 4*x - 90")  # Valor padrão

label_ponto = ttk.Label(frame_entrada, text="Ponto para calcular a derivada :")
label_ponto.grid(row=4, column=0, padx=5, pady=5)
entry_ponto = ttk.Entry(frame_entrada)
entry_ponto.grid(row=4, column=1, padx=5, pady=5)

label_inicio = ttk.Label(frame_entrada, text="Início do Intervalo:")
label_inicio.grid(row=1, column=0, padx=5, pady=5)
entry_inicio = ttk.Entry(frame_entrada)
entry_inicio.grid(row=1, column=1, padx=5, pady=5)

label_fim = ttk.Label(frame_entrada, text="Fim do Intervalo:")
label_fim.grid(row=1, column=2, padx=5, pady=5)
entry_fim = ttk.Entry(frame_entrada)
entry_fim.grid(row=1, column=3, padx=5, pady=5)

# Botão para calcular o ponto mínimo
botao_calcular_minimo = ttk.Button(frame_entrada, text="Calcular Ponto Mínimo", command=calcular_ponto_minimo)
botao_calcular_minimo.grid(row=2, column=0, padx=5, pady=5)

# Botão para atualizar o gráfico
botao_atualizar_grafico = ttk.Button(frame_entrada, text="Atualizar Gráfico", command=atualizar_grafico)
botao_atualizar_grafico.grid(row=2, column=1, padx=5, pady=5)


# Frame para exibir o gráfico
frame_grafico = ttk.Frame(app)
frame_grafico.pack(side=tk.TOP, padx=10, pady=10)


# Botão para obter o máximo
botao_maximo = ttk.Button(frame_entrada, text="Obter o máximo", command=calcular_ponto_maximo)
botao_maximo.grid(row=2, column=2, padx=5, pady=5)

# Botão para obter o mínimo
botao_minimo = ttk.Button(frame_entrada, text="Obter o mínimo", command=calcular_ponto_minimo)
botao_minimo.grid(row=2, column=3, padx=5, pady=5)

# Botão para obter a media
botao_media = ttk.Button(frame_entrada, text="Obtem o media", command=media)
botao_media.grid(row=3, column=1, padx=5, pady=5)

# Botão para obter o desvio padrão
botao_desvio = ttk.Button(frame_entrada, text="Obtem o desvio padrão", command=desvio_padrao)
botao_desvio.grid(row=3, column=2, padx=5, pady=5)

# Botão para obter a integral
botao_integral = ttk.Button(frame_entrada, text="Obtem a integral", command=area_integracao)
botao_integral.grid(row=3, column=0, padx=5, pady=5)

# Botão para obter as raízes
botao_raizes = ttk.Button(frame_entrada, text="Obtem as raízes", command=raizes)
botao_raizes.grid(row=3, column=3, padx=5, pady=5)

# Botão para obter a derivada num ponto
botao_derivada = ttk.Button(frame_entrada, text="Obtem a derivada num ponto", command=derivada)
botao_derivada.grid(row=3, column=3, padx=5, pady=5)






app.mainloop()





