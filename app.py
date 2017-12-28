from flask import Flask, render_template, request, redirect
import pandas as pd
import requests
import quandl
from bokeh.plotting import figure
from bokeh.embed import components
import simplejson

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# quandl.ApiConfig.api_key = "bbcN1HBxBVzay8-qxx7B"
# data = quandl.get(" WIKI/PRICES")

# @app.route('/graph')
# def graph():
#     return render_template('graph.html')


if __name__ == '__main__':
    app.run(port=33507)

