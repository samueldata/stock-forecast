from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
import subprocess
import sys

# Adicionar o diretório raiz do projeto ao PYTHONPATH
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, root_dir)

from src.analysis.explore_data import explore_data  # Certifique-se de que o caminho está correto

app = Flask(__name__)

# Diretório de resultados
results_dir = os.path.join(root_dir, 'results')

@app.route('/')
def index():
    # Carregar a lista de ações do CSV
    stock_list_path = os.path.join(root_dir, 'src', 'data', 'available_stocks.csv')
    stocks_df = pd.read_csv(stock_list_path)
    
    # Converter o DataFrame para um dicionário
    stocks = stocks_df.to_dict(orient='records')
    
    # Passar a lista de ações para o template
    return render_template('index.html', stocks=stocks)

@app.route('/forecast', methods=['POST'])
def forecast():
    stock = request.form.get('stock')

    # Executar download_data.py para baixar os dados da ação selecionada
    try:
        subprocess.run(['python', os.path.join(root_dir, 'src', 'data', 'download_data.py'), stock], check=True)
    except subprocess.CalledProcessError as e:
        return f'Erro ao baixar dados para {stock}: {str(e)}', 500

    # Executar forecast_model.py para gerar o gráfico interativo
    try:
        subprocess.run(['python', os.path.join(root_dir, 'src', 'modeling', 'forecast_model.py'), stock], check=True)
    except subprocess.CalledProcessError as e:
        return f'Erro ao gerar previsão para {stock}: {str(e)}', 500

    return redirect(url_for('display_forecast', stock=stock))

@app.route('/display_forecast')
def display_forecast():
    stock = request.args.get('stock')
    plot_path = os.path.join(results_dir, f'{stock}_forecast_plot.html')

    # Verificar se o gráfico existe
    if not os.path.exists(plot_path):
        return f'Gráfico para o estoque {stock} não encontrado.', 404

    # Carregar e renderizar o gráfico gerado
    with open(plot_path, 'rb') as plot_file:
        plot = plot_file.read().decode('utf-8')

    # Obter o resumo dos dados
    file_name = f'{stock.lower()}_historico.csv'
    file_path = os.path.join(root_dir, 'data', 'raw', file_name)
    if not os.path.isfile(file_path):
        return f'Arquivo de dados para {stock} não encontrado.', 404

    summary = explore_data(file_path)

    return render_template('forecast.html', plot=plot, summary=summary, stock=stock)

if __name__ == '__main__':
    app.run(debug=True)
