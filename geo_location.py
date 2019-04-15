
import requests
import geocoder

url = 'https://api.darksky.net/forecast/4b1aa4882b2d8ec3a573d48d615db4ea/'
g = geocoder.arcgis('Redlands, CA')

print(g.latlng)

places = [
'Space Needle',
'Crater Lake',
'Golden Gate Bridge',
'Yosemite National Park',
'Las Vegas, Nevada',
'Grand Canyon National Park',
'Aspen, Colorado',
'Mount Rushmore',
'Yellowstone National Park',
'Sandpoint, Idaho',
'Banff National Park',
'Capilano Suspension Bridge',
]

locations = []

api = requests.request('GET', url+str(g.latlng[0])+','+str(g.latlng[1]))

result = api.json()

currently = result['currently']
for place in places:
   g = geocoder.arcgis(place)
   locations.append(place)
   locations.append(g.latlng)
   print(f'{place} is located at {g.latlng[0]},{g.latlng[1]}\nAt{place} right now. it is {currently["summary"]} with a Temperature of {currently["temperature"]}')





