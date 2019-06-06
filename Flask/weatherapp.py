__author__ = 'Mark'
import pyowm
from flask import Flask
from flask import request
owm = pyowm.OWM('469b2ec82985f979ec625b93836c36bf')



app = Flask(__name__)
app.debug = True

#####Creates the function form_example under the first forward slash in this path
####first function asks for a city to input and takes that info to the next section

@app.route('/')
def form_example():
    html = ''
    html += "<hmtl> \n"
    html += "<body> \n"
    html += '<form method="POST" action="form_input">\n'
    html += 'Input a (City, Country) to check weather forecast: <input type="text" name ="city" /> \n'
    html += "<p> \n"
    html += '<input type="submit" value="submit" /> \n'
    html += "</form> \n"
    html += "</body> \n"
    html += "</html> \n"
    return html
#########the value is returned and then the weather info is done in this function
########takes the city string and makes a variable to get the weather for it
########make a variable for temp, humidity, and the forecast
@app.route('/form_input', methods=['POST'])
def form_input():
    city = request.form['city']
    obs = owm.weather_at_place(city)
    w = obs.get_weather()

    temp = w.get_temperature('fahrenheit')
    temp = str(temp)
    humidity = w.get_humidity()
    humidity = str(humidity)
    fc = owm.daily_forecast(city, limit=5)
    f = fc.get_forecast()

    html = ''
    html += '<html> \n'
    html += '<body> \n'
    html += 'Weather for:' + ' '+ city + ' ' + temp +  '\n'
    html += '<p>' + 'Humidity: ' + humidity + '</p>' + '\n'
    html += "Forecast for tomorrow: "
    for weather in f:

        a = weather.get_reference_time('iso'),weather.get_status(),weather.get_temperature('fahrenheit')
        a = str(a)
        html += '<p>' + a + '</p>'
        break
    html += 'Five Day Forecast: ' + '\n'
    for weather in f:

        a = weather.get_reference_time('iso'),weather.get_status(),weather.get_temperature('fahrenheit')
        a = str(a)
        html += '<p>' + a + '</p>'
    html += '\n'
    html += '</body> \n'
    html += '</hmtl> \n'
    return html
if __name__ == '__main__':
    app.run()