import numpy as np
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
import api

def datetime(x):
    return np.array(x, dtype=np.datetime64)

def plot_it_out(stock):
    p1 = figure(x_axis_type="datetime", title="Stock Closing Prices")
    p1.grid.grid_line_alpha=0.3
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Price'

    my_df = api.read_data(stock)
    p1.line(datetime(my_df.index), my_df['Close'], color='#000000', legend=stock)
    p1.legend.location = "top_left"

    output_file("graph.html", title="Graph of "+stock)
    show(gridplot([[p1]], plot_width=400, plot_height=400))

plot_it_out('GOOG')
plot_it_out('AMZN')
plot_it_out('FB')