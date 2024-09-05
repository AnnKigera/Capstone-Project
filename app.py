from flask import Flask, render_template
import mysql.connector
import pandas as pd

app = Flask(__name__)

def get_data():
    connection = mysql.connector.connect(
        host='localhost',
        database='scraper_db',
        user='root',
        password='your_password'
    )
    query = "SELECT * FROM products"
    df = pd.read_sql(query, connection)
    connection.close()
    return df

@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', tables=[data.to_html(classes='data')], titles=data.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
