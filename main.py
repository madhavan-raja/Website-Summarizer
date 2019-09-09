from flask import Flask, render_template, request
from flask_cors import CORS
import json

import summarize

error_message = "An error occoured while trying to reach the page."
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/main', methods=['POST'])
def main():
    print(request.method)
    data = request.data
    my_data = json.loads(data.decode("utf-8"))
    input_text = my_data['input_text']
    try:
        output = summarize.summarized(input_text)
    except:
        output = error_message
    return output

if __name__ == '__main__':
    app.run(debug=True)
