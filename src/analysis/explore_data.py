import pandas as pd
import os

def load_data(file_name):
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    file_path = os.path.join(root_dir, 'data', 'raw', file_name)
    return pd.read_csv(file_path, index_col='Date', parse_dates=True)

def explore_data(file_name):
    data = load_data(file_name)
    summary = {
        'head': data.head().to_html(),
        'describe': data.describe().to_html(),
        'missing': data.isnull().sum().to_frame().to_html()
    }
    return summary
