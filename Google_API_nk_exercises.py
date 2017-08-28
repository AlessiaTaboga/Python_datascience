# EXERCISES ON GOOGLE API:
# NOTE: You need to use your personal Google API key (not shown here in GitHub)


# EXERCISE 1:
# given n addresses
# we want to calculate the total distance of visiting all the addresses,
# assuming a particular order between them (as for a postman following his delivery route)

# address_list_in contains a list of n UK addresses
# given as strings ('street number, street name, city, country')

import googlemaps
gmaps = googlemaps.Client(key='put your Google key here')
from datetime import datetime

def total_route_distance(address_list_in):
    distance=[]
    n = len(address_list_in)
    for i in range(n-1):
        dir_xy=gmaps.directions(address_list_in[i],address_list_in[i+1], mode='transit',departure_time=datetime.now())
        distance_xy=int(dir_xy[0]['legs'][0]['distance']['value'])
        distance.append(distance_xy)
    tot_dist_km=(sum(distance))/1000
    print('The total distance in km is:', tot_dist_km)


# EXERCISE 2:
# design a function that takes two addresses
# and then returns a list of instructions for the shortest way (according to google)
# of navigating from address1 to address2

import googlemaps
gmaps = googlemaps.Client(key='put your Google key here')
from datetime import datetime

def get_route_instructions(address1,address2):
    dir_xy = gmaps.directions(address1, address2, mode='transit', departure_time=datetime.now())
    n1=len(dir_xy[0]['legs'][0]['steps'])
    for x in range(0,n1):
        print(dir_xy[0]['legs'][0]['steps'][x]['html_instructions'])
        if 'steps' in dir_xy[0]['legs'][0]['steps'][x]:
            n2 = len(dir_xy[0]['legs'][0]['steps'][x]['steps'])
            for y in range(0,n2):
                print(dir_xy[0]['legs'][0]['steps'][x]['steps'][y]['html_instructions'])