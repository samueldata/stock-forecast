import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from data.download_data import download_and_save_data

# import os
# from src.data.download_data import download_and_save_data

def test_download_and_save_data():
    ticker = "PETR4"  # Exemplo de ticker
    save_path = "test_petr4.csv"

    # Executar função de download
    download_and_save_data(ticker, save_path)

    # Verificar se o arquivo foi criado
    assert os.path.exists(save_path)

    # Remover arquivo após o teste
    os.remove(save_path)
