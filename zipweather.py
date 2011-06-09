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
        if condition == 'Sunny' or condition == 'Clear':
            image = 'Sunny.png'
        if condition == 'Thunderstorm' or \
           condition == 'Chance of TStorm' or \
           condition == 'Scattered Thunderstorms' or\
           condition == 'Chance of Storm' or\
           condition == 'Rain':
            image = 'Thunderstorm.png'
        if condition == 'Storm' or \
           condition == 'Showers' or \
           condition == 'Scattered Showers' or \
           condition == 'Chance of Rain':
            image = 'Rain.png'
        if condition == 'Light Rain':
            image = 'RainLight.png'
        if condition == 'Rain and Snow':
            image = 'RainSnow.png'
        if condition == 'Snow Showers' or \
           condition == 'Chance of Snow' or \
           condition == 'Snow':
            image = 'Snow.png'
        if condition == 'Light Snow' or condition == 'Flurries':
            image = 'SnowLight.png'
        if condition == 'Hail':
            image = 'Hail.png'
        if condition == 'Freezing Drizzle':
            image = 'FreezingDrizzle.png'
        if condition == 'Partly Sunny' or condition == 'Mostly Cloudy':
            image = 'MostlyCloudy.png'
        if condition == 'Mostly Sunny' or condition == 'Partly Cloudy':
            image = 'MostlySunny.png'
        if condition == 'Cloudy' or condition == 'Overcast':
            image = 'Cloudy.png'
        if condition == 'Sleet' or condition == 'Icy':
            image = 'Sleet.png'
        if condition == 'Mist':
            image = 'Mist.png'
        if condition == 'Fog':
            image = 'Fog.png'
        if condition == 'Smoke':
            image = 'Smoke.png'
        if condition == 'Dust' or condition == 'Haze':
            image = 'Dust.png'
        image = "../static/images/weather/"+image
        return render_template('weather.html', \
        zipcode=zipcode, valid=valid, weather=result,  image=image)
    except IndexError:
        valid = False
        return render_template('weather.html', \
        zipcode=zipcode, valid=valid,)
   

if __name__ == '__main__':
    app.debug = True
    app.run()
