from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import pywapi

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<zipcode>/')
def weather(zipcode):
    valid = True
    try:
        result = pywapi.get_weather_from_google(zipcode)
        cur_temp=result['current_conditions']['temp_f']
        city=result['forecast_information']['city']
        return render_template('weather.html', zipcode=zipcode, city=city, cur_temp=cur_temp, valid=valid)
    except IndexError:
        valid = False
        return render_template('weather.html', zipcode=zipcode)
   

if __name__ == '__main__':
    app.debug = True
    app.run()
