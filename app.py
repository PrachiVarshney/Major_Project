from flask import Flask, render_template, request
from flask import url_for
import pandas as pd

app = Flask(__name__)
df = pd.read_csv(r'D:\Project\rideshare_kaggle.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/price_prediction')
def price_prediction():
    return render_template('price_prediction.html')

@app.route('/analysis_insights')
def analysis_insights():  # Updated route for Analysis Insights
    return render_template('analysis_insights.html')

@app.route('/Blog')
def Blog():  # Updated route for Blog
    return render_template('Blog.html')

@app.route('/calculate', methods=['POST'])
def calculate_price():
    source = request.form['source']
    destination = request.form['destination']
    cab_type = request.form['cab_type']

    price = df[(df['source'] == source) & (df['destination'] == destination) & (df['cab_type'] == cab_type)]['price'].values
    if len(price) > 0:
        price = price[0]
    else:
        price = 'N/A'

    return render_template('result.html', source=source, destination=destination, cab_type=cab_type, price=price)

def analyze_availability(hour):
    hour = int(hour)
    if 6 <= hour < 12:
        return "High availability"
    elif 12 <= hour < 18:
        return "Moderate availability"
    elif 18 <= hour < 24:
        return "Low availability"
    else:
        return "Limited availability"

if __name__ == '__main__':
    app.run(debug=True)
