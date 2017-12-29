from flask import Flask, render_template, request, redirect
import api_plot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/', methods=['POST'])
# def read_post():
#     text = request.form['ticker']
#     processed_text = text.upper()
#     api_plot.plot_it_out(processed_text)
#     return render_template('stockplot.html')

if __name__ == '__main__':
    app.run(port=33507)



