# requests is part of the python standard library
import requests

'''
Author: Derrick Ortiz
Description: The purpose of this program is to use the Census Bureau
free API to retrieve the GPS coordinates of a home address. A process
known as 'Geocoding'

Note 1: I use f-strings throughout for readability 
Note 2: if you delete all of the docstrings and comments, you will find a very lean script.
Note 3: here is some information on http requests 'https://requests.readthedocs.io/en/latest/'
Note 4: Documentation on Geocoding from the Census Bureau 'https://geocoding.geo.census.gov/geocoder/'
'''

# The Address of the residence you would like to geocode. 
# Default is Griffith Observatory: 
# 2800 E Observatory Rd, Los Angeles, CA 90027
address ="2800 E Observatory Rd, Los Angeles, CA 90027"

try:
    # this is the url for our Census api, notice I've inserted the address. I used an f-string here
    url = f"https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address={address}&benchmark=2020&format=json"

    # Make an http request to the API and store the response object
    response = requests.get(url) 

    '''
    # printing the response object gives you the code 200 if it is successful
    # this is an unnessesary step
    
    print(response)
    '''

    # we parse the response as a json object
    result = response.json()

    '''
    # if you print the parsed object, you get a dictionary as a string
    # JSON objects are just dicts. The print statement is ugly and hard to read
    # but you can do that here if you are curious
    # You will also notice that Census gave us a ton of information we don't plan on using

    print(result)

    # to print the full JSON response in a way that is easier to read
    # import the pretty printer module

    from pprint import pprint
    pprint(result)

    # hint, save the above two lines of code for working with JSON in the future, it's very useful
    '''


    # result has a lot of information we didn't need, so we are storing the part we are interested in.
    # To see how I came to write the code beneath, pretty print the result using the above commented code and find 'coordinates'
    coords = result['result']['addressMatches'][0]['coordinates']

    '''
    # At this point we already have what we wanted... The gps coordinates are stored in the coords variable
    # the rest of the code is just to isolate the values in usable way.
    # you can print the coords now to see why we go through the extra work below

    print(coords)    
    '''

    # just some extra work here for the sake of sanity
    # Labeling my values for easier manipulation
    latitude = coords['y']
    longitude = coords['x']

    '''
    # here is a sample where we limit to only 5 trailing decimals using f-strings
    latitude = f"{coords['y']:.5f}"
    longitude = f"{coords['x']:.5f}"
    '''

    print('\n') 
    print('Latitude: ', latitude)
    print('Longitude: ', longitude)


except:
    print("Invalid URL or some error occured while making the GET request to the specified URL")

