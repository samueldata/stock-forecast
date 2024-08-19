import yfinance as yf
import os
from datetime import datetime, timedelta
import sys

# Definir diretório raiz do projeto
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Calcular datas dinâmicas
hoje = datetime.now()
data_fim = hoje.strftime('%Y-%m-%d')
data_inicio = (hoje - timedelta(days=365*10)).strftime('%Y-%m-%d')

# Diretório para salvar os dados
save_dir = os.path.join(root_dir, 'data', 'raw')
os.makedirs(save_dir, exist_ok=True)

# Função para baixar e salvar os dados
def download_and_save_data(ticker, save_path):
    print(f"Baixando dados para {ticker}...")
    dados = yf.download(ticker, start=data_inicio, end=data_fim)
    
    # Remover dias de final de semana e salvar
    dados = dados.dropna()
    dados.to_csv(save_path)
    print(f"Dados históricos de {ticker} salvos em: {save_path}")

if __name__ == "__main__":
    # Receber o símbolo da ação como argumento
    if len(sys.argv) != 2:
        print("Uso: python download_data.py <symbol>")
        sys.exit(1)
    
    symbol = sys.argv[1]
    ticker = symbol + '.SA'  # Adiciona o sufixo '.SA' para o Yahoo Finance
    save_path = os.path.join(save_dir, f'{symbol}_historico.csv')
    download_and_save_data(ticker, save_path)
