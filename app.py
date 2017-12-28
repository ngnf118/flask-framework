from flask import Flask, render_template, request, redirect
import pandas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/graph')
# def stock_to_df(my_string):
#     something

if __name__ == '__main__':
    app.run(port=33507)

