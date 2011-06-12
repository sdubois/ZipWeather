from flask import Flask, request, session, g, redirect, \
url_for, abort, render_template, flash
import pywapi

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        zipcode = request.form['zipcode']
        print "zipcode"+zipcode
        if zipcode == "":
            return render_template('weather.html', zipcode=zipcode, \
            valid=False)
        else:
            return redirect(url_for('weather', zipcode=zipcode))
    return render_template('index.html')

@app.route('/<zipcode>/')
def weather(zipcode):
    boolzip = zipcode.isdigit()
    if boolzip:
        valid = True
    else:
        valid = False
    try:
        result = pywapi.get_weather_from_google(zipcode)
        condition = result['current_conditions']['condition']
        options = {
            'Sunny': 'Sunny.png',
            'Clear': 'Sunny.png',
            'Thunderstorm': 'Thunderstorm.png',
            'Chance of TStorm' : 'Thunderstorm.png',
            'Scattered Thunderstorms': 'Thunderstorm.png',
            'Chance of Storm': 'Thunderstorm.png',
            'Rain': 'Thunderstorm.png',
            'Storm': 'Rain.png', 
            'Showers': 'Rain.png', 
            'Scattered Showers': 'Rain.png', 
            'Chance of Rain': 'Rain.png', 
            'Light Rain': 'RainLight.png',
            'Rain and Snow': 'RainSnow.png',
            'Snow Showers': 'Snow.png',
            'Chance of Snow': 'Snow.png',
            'Snow': 'Snow.png',
            'Light Snow': 'SnowLight.png',
            'Flurries': 'SnowLight.png',
            'Hail': 'Hail.png',
            'FreezingDrizzle': 'FreezingDrizzle.png',
            'Partly Cloudy': 'MostlyCloudy.png',
            'Mostly Sunny': 'MostlyCloudy.png',
            'Mostly Sunny': 'MostlySunny.png',
            'Partly Cloudy': 'MostlySunny.png',
            'Cloudy': 'Cloudy.png',
            'Overcast': 'Cloudy.png',
            'Sleet': 'Sleet.png',
            'Icy': 'Sleet.png',
            'Mist': 'Mist.png',
            'Fog': 'Fog.png',
            'Smoke': 'Smoke.png',
            'Dust': 'Dust.png',
            'Haze': 'Dust.png',}
        image = "../static/images/weather/"+options[condition]
        return render_template('weather.html', \
        zipcode=zipcode, valid=valid, weather=result,  image=image)
    except IndexError:
        valid = False
        return render_template('weather.html', \
        zipcode=zipcode, valid=valid,)
   

if __name__ == '__main__':
    app.debug = True
    app.run()
