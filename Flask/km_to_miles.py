__author__ = 'Mark'
from flask import Flask
from flask import request

app = Flask(__name__)
app.debug = True

#####Creates the function form_example under the first forward slash in this path
#####The function puts all of the html to ask the user to input a distance in kilometers
#####There is a button that allows user to input a number and then it submits to the next page
@app.route('/')
def form_example():
    html = ''
    html += "<hmtl> \n"
    html += "<body> \n"
    html += '<form method="POST" action="form_input">\n'
    html += 'Input a distance in kilometers: <input type="text" name ="kilometers" /> \n'
    html += "<p> \n"
    html += '<input type="submit" value="submit" /> \n'
    html += "</form> \n"
    html += "</body> \n"
    html += "</html> \n"
    return html
#########the value is returned and then all of the variable math is done in this function

@app.route('/form_input', methods=['POST'])
def form_input():
    kilometers = request.form['kilometers']
    kilometers = int(kilometers)
    miles = 0.621371 * kilometers
    miles = str(miles)
    kilometers = str(kilometers)
    html = ''
    html += '<html> \n'
    html += '<body> \n'
    html += 'You entered:' + ' ' + kilometers + ' ' + "kilometers." + \
            " " + ' The equivalent in miles is ' + " " + miles + " " + \
            "miles" + '\n'
    html += '</body> \n'
    html += '</hmtl> \n'
    return html
if __name__ == '__main__':
    app.run()