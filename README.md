# Stock Forecast Application

## Objective

The Stock Forecast project is a web application developed to analyze and predict the future behavior of stock prices using historical data. The application uses the `Prophet` library to create forecasting models and the `Plotly` library to generate interactive charts.

## Capabilities and Features

- **Data Analysis:** Loads and displays historical stock data.
- **Price Forecasting:** Uses the `Prophet` model to predict future stock prices.
- **Interactive Charts:** Generates interactive charts of historical prices and forecasts using `Plotly`.
- **Web Interface:** Provides a user-friendly web interface built with `Flask` for interaction.
- **Results Visualization:** Displays charts and data summaries directly within the web application.

## Project Structure

- **`app.py`**: Main Flask application file that manages routes and backend logic.
- **`src/data/download_data.py`**: Script to download historical stock data.
- **`src/modeling/forecast_model.py`**: Script to generate forecasting model and interactive chart.
- **`src/analysis/explore_data.py`**: Script to explore and summarize historical data.
- **`configs/config.yaml`**: Configuration file (optional).
- **`configs/secrets.yaml`**: File for secrets and credentials (optional).
- **`results/`**: Directory to store generated charts and results.
- **`templates/`**: Directory for HTML template files.

## Running the Application

### Prerequisites

Make sure you have `Python` and `pip` installed. You will also need a virtual environment to install dependencies.

### Setting Up the Environment

1. **Clone the Repository**

   ```sh
   git clone <REPOSITORY_URL>
   cd stock-forecast
   ```

2. **Create and Activate a Virtual Environment**
   
   ```sh
   python -m venv venv
   source venv/bin/activate  # For Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Start the Application**
   ```sh
   python main.py
   ```

## Usage

### Home Page

- **Select a Stock**: From the dropdown menu, choose a stock symbol to analyze.
- **Submit**: Click the "Submit" button to start the data processing and forecasting.

### Forecast Page

- **View Forecast**: The page will display an interactive chart showing the historical and forecasted stock prices.
- **Data Summary**: A summary of the historical data, including statistics and trends, will also be displayed below the chart.

### Additional Features

- **Download Data**: Historical data for the selected stock is fetched from Yahoo Finance and saved locally.
- **Interactive Charts**: Use the interactive features of Plotly charts to zoom in, hover for details, and explore the forecasted data.

## Troubleshooting

- **Application Not Running**: Ensure that all dependencies are installed and that `main.py` is executed in the virtual environment.
- **Chart Not Displaying**: Verify that the `results/` directory contains the generated HTML files and that they are correctly linked.
- **Errors in Data Download**: Check the logs for any issues related to data fetching and verify the stock symbol.

## Frequently Asked Questions

- **How do I add more stocks to the application?**
  Update the `available_stocks.csv` file in the `src/data/` directory with new stock symbols and company names.

- **Can I customize the forecasting model?**
  Yes, you can modify the `forecast_model.py` script to adjust the parameters and configuration of the Prophet model.

- **How do I contribute to the project?**
  Follow the guidelines in the Contributing section above to submit improvements or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or support, please reach out to [datasamuel@outlook.com](mailto:datasamuel@outlook.com).
