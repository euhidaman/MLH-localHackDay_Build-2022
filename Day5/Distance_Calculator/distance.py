from geopy.geocoders import Nominatim
from geopy import distance


def maps_dir(startPoint, destPoint):

    try:
        geocoder = Nominatim(user_agent='Nuvia')

        start_coord = geocoder.geocode(startPoint)
        dest_coord = geocoder.geocode(destPoint)

        start_location = (start_coord.latitude, start_coord.longitude)
        dest_location = (dest_coord.latitude, dest_coord.longitude)
        total = distance.great_circle(start_location, dest_location).km
        print(
            f'Total Distance between the two cities : {round(total, 2)} Kilometers')

    except Exception as e:
        return 'none'


city1 = input('Enter your starting city : ')
city2 = input('Enter your destination city : ')

maps_dir(city1, city2)
