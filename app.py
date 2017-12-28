from flask import Flask, render_template, request, redirect
import pandas as pd
import requests
from bokeh.plotting import figure
from bokeh.embed import components

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph')
def graph():
    api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json' % stock
    session = requests.Session()
    session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
    raw_data = session.get(api_url)
    # my_df = pd.DataFrame(raw_data)
    plot = figure(tools=TOOLS,
                  title='Data from Quandle WIKI set',
                  x_axis_label='date',
                  x_axis_type='datetime')
    script, div = components(plot)
    return render_template('graph.html', script=script, div=div)

if __name__ == '__main__':
    app.run(port=33507)

