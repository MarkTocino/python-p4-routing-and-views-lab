#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join(str(i) for i in range(parameter + 1))
    return numbers
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        result =  num1 + num2
    elif operation == "-":
        result =  num1 - num2
    elif operation == "*":
        result =  num1 * num2
    elif operation == 'div':
        result =  num1/num2
    elif operation == '%':
        result =  num1 % num2
    else:
        return None
    return f'{result}'