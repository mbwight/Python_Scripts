__author__ = 'Mark'
from flask import Flask
from flask import request

app = Flask(__name__)
app.debug = True

#####Creates the function form_example under the first forward slash in this path

@app.route('/')
def form_example():
    html = ''
    html += "<hmtl> \n"
    html += "<body> \n"
    html += '<form method="POST" action="form_input">\n'
    html += 'Add words to a dictionary: <input type="text" name ="dictionary" /> \n'
    html += "<p> \n"
    html += '<input type="submit" value="submit" /> \n'
    html += "</form> \n"
    html += "</body> \n"
    html += "</html> \n"
    return html


@app.route('/form_input', methods=['POST'])
def form_input():
    dictionary = request.form['dictionary']



    dictionary1 = dictionary.split(" ")

    newdict = {}
    for i in dictionary1:

        i = i.lower()
        key = newdict.get(i)
        if i not in newdict:
            newdict[i] = 1
        else:
            newdict[i] = key + 1


    html = ''

    html += '<html> \n'
    html += '<body> \n'
    html += ("<!DOCTYPE html>" + '\n' + "<html>" + '\n' + "<head>" + '\n'
             + "</head>" + '\n' + "<body>" + '\n' + "<table>" + '\n' +
             "<tr>" + '\n' + "<th>" + "Words" + "</th>" + "<th>" + "Count"
             + "<th>" + '\n')
    for i in newdict:
         html +=  ("<tr>" + "<td>" + i + "</td>" + " " + "<td>" +str(newdict.get(i))
                         + "</td>" + "</tr>" + '\n')





    html += '</body> \n'
    html += '</hmtl> \n'
    return html
if __name__ == '__main__':
    app.run()