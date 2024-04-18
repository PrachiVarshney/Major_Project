from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
df = pd.read_csv(r'D:\ll\rideshare_kaggle.csv')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/price_prediction')
def price_prediction():
    return render_template('price_prediction.html')

@app.route('/weather_check')
def weather_check():
    return render_template('weather_check.html')

@app.route('/cab_type')
def cab_type():
    return render_template('cab_type.html')

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
