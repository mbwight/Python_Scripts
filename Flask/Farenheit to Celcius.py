__author__ = 'Mark'
from flask import Flask
from flask import request

app = Flask(__name__)
app.debug = True

@app.route('/')
def form_example():
    html = ''
    html += "<hmtl> \n"
    html += "<body> \n"
    html += '<form method="POST" action="form_input">\n'
    html += 'Input a temperature in Farenheit: <input type="text" name ="farenheit" /> \n'
    html += "<p> \n"
    html += '<input type="submit" value="submit" /> \n'
    html += "</form> \n"
    html += "</body> \n"
    html += "</html> \n"
    return html
@app.route('/form_input', methods=['POST'])
def form_input():

    farenheit = request.form['farenheit']
    farenheit = int(farenheit)
    celsius = 5/9 * (farenheit - 32)
    celsius = str(celsius)
    farenheit = str(farenheit)
    html = ''
    html += '<html> \n'
    html += '<body> \n'
    html += 'Farenheit to Celcius:' + farenheit + ' to ' + celsius + '\n'
    html += '</body> \n'
    html += '</hmtl> \n'
    return html
if __name__ == '__main__':
    app.run()