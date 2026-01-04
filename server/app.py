from flask import Flask

app = Flask(__name__)

# Index route
@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# Print string route
@app.route("/print/<string:param>")
def print_string(param):
    print(param)  # prints to console
    return param  # return exactly what the test expects

# Count numbers route
@app.route("/count/<int:number>")
def count(number):
    output = ""
    for i in range(number):  # start from 0
        output += f"{i}\n"
    return output

# Math operations route
@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        if num2 == 0:
            return "Cannot divide by zero"
        result = num1 / num2  # always float
        return str(result)    # return float string immediately
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid operation"

    # For other operations, return integer string if no decimal part
    if result == int(result):
        return str(int(result))
    return str(result)
