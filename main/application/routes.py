from flask import Flask
from flask import render_template, request, requests


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/number', methods=['GET', 'POST'])
def number():
    formData = request.form.get('input')
    formData = int(formData)
    fizzBuzz = requests.post(f'http://fizzBuzz:5001/number/{formData}')
    factorial = requests.post(f'http://factorial:5002/number/{formData}')
    return render_template('output.html', originalInput=formData, threeFive=fizzBuzz, reversePrime=factorial)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)