from flask import Flask, render_template, request
from wise_quote import get_wise_quote
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        source_currency = request.form['source_currency'].upper()
        target_currency = request.form['target_currency'].upper()
        source_amount = float(request.form['source_amount'])

        quote_data = get_wise_quote(source_currency, target_currency, source_amount)
        logging.debug(f"Quote Data: {quote_data}")

        return render_template('index.html', quote_data=quote_data)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)