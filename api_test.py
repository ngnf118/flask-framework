from flask import Flask, render_template, request, redirect
import quandl
import numpy as np
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components

def read_data(stock):
    quandl.ApiConfig.api_key = "bbcN1HBxBVzay8-qxx7B"
    data = quandl.get("WIKI/"+stock, start_date="2017-11-01", end_date="2017-11-30")
    # print(data.head())
    return data

def datetime(x):
    return np.array(x, dtype=np.datetime64)

def plot_it_out(stock):
    p1 = figure(x_axis_type="datetime", title="Stock Closing Prices")
    p1.grid.grid_line_alpha = 0.3
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Price'

    my_df = read_data(stock)
    p1.line(datetime(my_df.index), my_df['Close'], color='#000000', legend=stock)
    p1.legend.location = "top_left"

    output_file("templates/stockplot.html", title="Graph of " + stock)
    show(gridplot([[p1]], plot_width=400, plot_height=400))
    return
    # script, div = components(p1)
    # return render_template('stockplot.html', script=script, div=div)

plot_it_out('GOOG')
plot_it_out('AMZN')
plot_it_out('FB')