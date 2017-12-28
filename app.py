from flask import Flask, render_template, request, redirect
import pandas

def stock_to_df(my_string):
    return

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph')
def graph():
    return render_template('graph.html')

if __name__ == '__main__':
    app.run(port=33507)

