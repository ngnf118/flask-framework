import quandl
import pandas as pd
import numpy

def read_data(stock):
    quandl.ApiConfig.api_key = "bbcN1HBxBVzay8-qxx7B"
    data = quandl.get("WIKI/"+stock, start_date="2017-11-01", end_date="2017-11-30")
    # print(data.head())
    return data

read_data("GOOG")
read_data("AMZN")
read_data("FB")



