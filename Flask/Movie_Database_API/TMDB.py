__author__ = 'Mark'

#######import the movie data base and add API key that I received
import tmdbsimple as tmdb
tmdb.API_KEY = 'be5e02bbfafa5a2a585cdfe2c7d208a2'

######import flask features to make online web app
from flask import Flask
from flask import request


app = Flask(__name__)
app.debug = True

##########the first page of the web app has html stored in a variable
##########there is code to have a user input via a submit button where they search
##########a movie and then the html is returned
@app.route('/')
def form_example():
    html = ''
    html += "<hmtl> \n"
    html += "<body> \n"
    html += '<form method="POST" action="form_input">\n'
    html += 'Welcome to The Movie Data Base. Enter a Movie Title to Search For: <input type="text" name ="movie_title" /> \n'
    html += "<p> \n"
    html += '<input type="submit" value="submit" /> \n'
    html += "</form> \n"
    html += "</body> \n"
    html += "</html> \n"
    return html
#######route for page 2. There is a function to take the data from movie_title
######there is a variable to search for the movie based on the user input variable
#######there is html to make a table based on the results of the movies found
@app.route('/form_input', methods=['POST'])
def form_input():
    movie_title = request.form['movie_title']
    search = tmdb.Search()
    response = search.movie(query=movie_title)

    html = ''
    html += '<html> \n'
    html += '<body> \n'
    html += 'Search Results For: ' + "'" + movie_title + "'" +  '\n'
    html += '<table>' + '\n' + "<tr>" + '\n' \
            + "<th>" + "Title" + "</th>" + "<th>" + "Release Date"+ "</th>" +\
            "<th>" + "Popularity"+ "</th>" + "<th>" + "Movie ID"+ "</th>"+'\n'

    for result in search.results:
        if result['release_date'] == '':
            result['release_date'] = "N/A"
        html += '<tr>'
        html += '<td>' + result['title'] + '</td>'
        html += '<td>' + result['release_date'] + '</td>'
        html += '<td>' + str(result['popularity']) + '</td>'
        html += '<td>' + str(result['id']) + '</td>'
        html += '</tr>'
        html += " "
        html += '\n'
    html += '</table>'
    html += '<a href="/">Back</a>'
    html += '</body> \n'
    html += '</hmtl> \n'
    return html

if __name__ == '__main__':
    app.run()
