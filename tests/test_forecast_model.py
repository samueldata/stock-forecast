import pytest
import pandas as pd
from modeling.forecast_model import create_forecast_model

def test_create_forecast_model():
    # Dados simulados
    mock_data = pd.DataFrame({
        "ds": ["2024-01-01", "2024-01-02", "2024-01-03"],
        "y": [100, 110, 105]
    })
    
    # Teste se o modelo é criado sem erros
    try:
        model, forecast = create_forecast_model(mock_data)
    except Exception as e:
        pytest.fail(f"Falha ao criar o modelo: {e}")
    
    # Teste se o retorno contém as chaves esperadas
    assert "yhat" in forecast.columns