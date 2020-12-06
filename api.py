from flask import Flask
from flask.globals import request
from flask.templating import render_template
from geopy.geocoders import Nominatim 


app = Flask(__name__)


@app.route('/')
def read_root():
    return render_template("blog-layout.html")


@app.route('/api/like', methods=['POST'])
def add_like():

    # initialize Nominatim API 
    geolocator = Nominatim(user_agent="geoapiExercises") 

    # Latitude & Longitude input 
    Latitude = request.args.get('lat')
    Longitude = request.args.get('lon')

    location = geolocator.reverse(Latitude+","+Longitude) 
    address = location.raw['address'] 

    # traverse the data 
    country = address.get('country', '') 
    code = address.get('country_code', '') 

    # find the country
    country_list = {
    "India": 1,
    "Canada": 2, 
    "Australia": 3, 
    }

    value = country_list.get(country)

    # get score

    # update the database

    # redirect to the same page


    return {'score':str(value)}

    #return render_template('login.html', msg="naveen")


if __name__ == '__main__':

    app.run(debug=True)


