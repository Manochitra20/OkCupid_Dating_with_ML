from flask import Flask
app = Flask(__name__)

# Create an instance of Flask
import dash_core_components as pip
import dash_html_components as html
import plotly.express as px
import pandas as pd


# Route to the basic info
@app.route('/chart')
def chart():
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/...')
    fig = px.sunburst(starbucks_dist, path=["okcupid", "location", "job", "offspring", ], values='Count',
                  title="Sunburst OkCupid", width=1000, height=800)
    fig.show()(df, x='Date', y='AAPL.High')
    return  html.Div([dcc.Graph(figure=fig)])