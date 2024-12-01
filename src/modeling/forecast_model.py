import os
import pandas as pd
import yfinance as yf
from prophet import Prophet
import plotly.graph_objects as go
import sys
from holidays.countries import Turkey

# Definir diretório raiz do projeto
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Função para baixar os dados históricos de uma ação
def fetch_stock_data(symbol):
    stock = yf.Ticker(symbol + '.SA')
    data = stock.history(period='max')
    data.reset_index(inplace=True)
    
    # Remover informações de fuso horário das datas
    if data['Date'].dt.tz is not None:
        data['Date'] = data['Date'].dt.tz_localize(None)
        
    data.rename(columns={'Date': 'ds', 'Close': 'y'}, inplace=True)
    return data[['ds', 'y']]

# Função para criar e salvar o modelo de previsão
def forecast_stock(data, symbol):
    model = Prophet()
    model.fit(data)
    future = model.make_future_dataframe(periods=365)
    forecast = model.predict(future)
    
    # Plotar previsões com Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['ds'], y=data['y'],
                             mode='lines', name='Dados Históricos'))
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'],
                             mode='lines', name='Previsão'))
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_lower'],
                             fill=None, mode='lines', line_color='lightgray',
                             name='Intervalo Inferior'))
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_upper'],
                             fill='tonexty', mode='lines', line_color='lightgray',
                             name='Intervalo Superior'))

    fig.update_layout(title=f'Previsões de Preços de {symbol}',
                      xaxis_title='Data',
                      yaxis_title='Preço de Fechamento',
                      template='plotly_dark')
    
    # Salvar gráfico interativo
    results_dir = os.path.join(root_dir, 'results')
    os.makedirs(results_dir, exist_ok=True)  # Cria o diretório se não existir
    fig_path = os.path.join(results_dir, f'{symbol}_forecast_plot.html')
    fig.write_html(fig_path)
    print(f'Gráfico interativo salvo em {fig_path}')

# Função para criar o modelo de previsão
def create_forecast_model(data):
    model = Prophet()
    model.fit(data)
    future = model.make_future_dataframe(periods=365)
    forecast = model.predict(future)
    return model, forecast

if __name__ == "__main__":
    # Receber o símbolo da ação como argumento
    if len(sys.argv) != 2:
        print("Uso: python forecast_model.py <symbol>")
        sys.exit(1)
    
    symbol = sys.argv[1]
    data = fetch_stock_data(symbol)
    forecast_stock(data, symbol)
