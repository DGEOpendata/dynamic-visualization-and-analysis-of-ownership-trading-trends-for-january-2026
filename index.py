python
import pandas as pd
from flask import Flask, render_template, request
import plotly.express as px

# Load dataset
data_url = "https://data.abudhabi/api/ownership-trading-summary-jan26.xlsx"
data = pd.read_excel(data_url)

# Flask application
app = Flask(__name__)

@app.route('/')
def index():
    # Generate summary metrics
    total_trading_value = data['Total Trading Value'].sum()
    foreign_trading_volume = data[data['Category'] == 'Foreign']['Volume'].sum()
    local_trading_volume = data[data['Category'] == 'Local']['Volume'].sum()
    
    return render_template('index.html', 
                           total_trading_value=total_trading_value,
                           foreign_trading_volume=foreign_trading_volume,
                           local_trading_volume=local_trading_volume)

@app.route('/chart')
def chart():
    # Generate interactive chart
    fig = px.bar(data, x='Category', y='Net Buy-Sell Difference', 
                 title='Net Buy-Sell Difference by Category', 
                 labels={'Net Buy-Sell Difference': 'Net Difference (AED)'}).to_html()
    return render_template('chart.html', chart=fig)

if __name__ == '__main__':
    app.run(debug=True)
