import requests
import pandas as pd

def fetch_stock_list():
    # Substitua o URL abaixo pela URL da API real que você utilizará
    url = 'https://api.example.com/stocks'  # Exemplo fictício
    response = requests.get(url)
    data = response.json()
    
    # Estrutura do JSON de resposta esperada: [{'symbol': 'PETR4', 'name': 'Petróleo Brasileiro S.A.'}, ...]
    stocks = pd.DataFrame(data)
    
    # Salva o DataFrame em um CSV
    stocks.to_csv('data/available_stocks.csv', index=False)

if __name__ == '__main__':
    fetch_stock_list()
