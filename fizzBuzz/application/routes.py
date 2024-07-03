from flask import Flask, Response, jsonify
import json
from flask import json
import sys
from flask import jsonify

app = Flask(__name__)

@app.route('number/<input>', methods=['GET', 'POST'])
def fizzBuzz(input):
    fizzBuzz = ''
    try:
        input = int(float(input))
    except ValueError:
        return "ValueError: please enter a number"
    if input % 3 == 0 and input % 5 == 0:
        fizzBuzz = 'fizz buzz'
    elif input % 3 == 0:
        fizzBuzz = 'fizz'
    elif input % 5 == 0:
        fizzBuzz = 'buzz'
    else:
        return input
    return fizzBuzz