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
    valid = True
    try:
        result = pywapi.get_weather_from_google(zipcode)    
        return render_template('weather.html', \
        zipcode=zipcode, valid=valid, weather=result)
    except IndexError:
        valid = False
        return render_template('weather.html', \
        zipcode=zipcode, valid=valid)
   

if __name__ == '__main__':
    app.debug = True
    app.run()
