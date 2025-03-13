from app import app

@app.route('/hello')
def hello():
    return "Hello, world!"

@app.route('/info')
def info():
    return "This is an informational page."

@app.route('/calc/<num1>/<num2>')
def calc(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        return 'Parameters are not int'
    return f'The sum of {num1} and {num2} is {sum([num1, num2])}.'

@app.route('/reverse/', defaults={'text': ''})
@app.route('/reverse/<string:text>')
def reverse(text):
    if text:
        return text[::-1]
    else:
        return 'Вы не ввели строку'

@app.route('/user/<name>/<age>')
def user(name, age):
    try:
        age = int(age)
        if int(age) >= 0:
            return f'Hello, {name}. You are {age} years old.'
        else:
            return 'Age cannot be less than 0'
    except ValueError:
        return 'Age is not int'