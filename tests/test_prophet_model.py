from src.modeling.forecast_model import create_forecast_model
import pandas as pd

def test_prophet_model_output():
    # Dados simulados
    mock_data = pd.DataFrame({
        "ds": pd.date_range(start="2024-01-01", periods=10),
        "y": [x for x in range(10)]
    })
    model, forecast = create_forecast_model(mock_data)
    
    # Verificar se há previsões para todas as datas
    assert len(forecast) > 0, "Nenhuma previsão foi gerada"
    assert "yhat" in forecast.columns, "Coluna 'yhat' não encontrada nas previsões"
