import os
from src.data.download_data import download_and_save_data

def test_download_and_save_data():
    ticker = "PETR4"  # Exemplo de ticker
    save_path = "test_petr4.csv"

    # Executar função de download
    download_and_save_data(ticker, save_path)

    # Verificar se o arquivo foi criado
    assert os.path.exists(save_path)

    # Remover arquivo após o teste
    os.remove(save_path)
