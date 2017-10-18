import requests

URL = "http://maps.googleapis.com/maps/api/geocode/json"
location = input()
PARAMS = {'address':location}
r = requests.get(URL, PARAMS)
data = r.json()
latitute = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']
print("The latitude is: %s\nThe Longitude is: %s\nThe full address is: %s" % (latitute,longitude,formatted_address))
