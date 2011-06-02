from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import pywapi
import pprint

pp = pprint.PrettyPrinter(indent=4)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<zipcode>/')
def weather(zipcode):
    result = pywapi.get_weather_from_google(zipcode)
    cur_temp=result['current_conditions']['temp_f']
    city=result['forecast_information']['city']
    return render_template('weather.html', zipcode=zipcode, city=city, cur_temp=cur_temp)

if __name__ == '__main__':
    app.debug = True
    app.run()
