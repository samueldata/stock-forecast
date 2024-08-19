import subprocess
import webbrowser
import time
import os

# Define o caminho para o script Flask
app_path = os.path.join(os.path.dirname(__file__), 'src', 'webapp', 'app.py')

# Define a URL padrão onde o Flask estará ouvindo
url = 'http://127.0.0.1:5000/'

# Função para iniciar o servidor Flask
def start_flask_app():
    # Executa o servidor Flask em um subprocesso
    subprocess.Popen(['python', app_path])

# Função para abrir o navegador
def open_browser():
    # Aguarda um momento para garantir que o servidor Flask esteja iniciado
    time.sleep(2)
    webbrowser.open(url)

if __name__ == '__main__':
    start_flask_app()
    open_browser()
