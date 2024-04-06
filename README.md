# cis6930sp24 -- Assignment2

Name: Suraj Kolla


UFID: 55496352


Email: n.kolla@ufl.edu


# Description
Download Incident Summary PDF files from the Norman Police Department website, extract relevant information, augment the extracted information to train a predictive model in the future.



## How to Install
`pipenv install`


## How to run
`pipenv run python assignment2.py --urls <url file name>`


<!-- video -->

https://github.com/CaptainO5/cis6930sp24-assignment2/assets/48147068/b3b28d11-f292-45d7-90b4-071b6ca2b0d6




## How to run tests


`pipenv run python -m pytest`


<!-- video -->

https://github.com/CaptainO5/cis6930sp24-assignment2/assets/48147068/905066ea-7dd6-4b17-8fc8-d01adca9101a





## Functions
#### assignment2.py\
This is the starting point of the program, which parses the command-line input URL File and send it to main

##### main()
Iterate over the urls, download the files and call augment data funciton before printing it to the stdout.
Prints the header once, prints the augmented data in the order of their appearance.

#### src/fetch.py\
##### download()
Uses the urlib library to download the given pdf and returns the location accessible to the extractor.


#### src/extract.py\
##### get_text_from() 
Takes a PDF file path, reads it, and convets it into a string. It also does preliminary filtering to remove headers and other unnecessary content that is specific to the Norman PD Incident Summaries.


##### parse()
Makes use of the Regular Expression module `re` in Python to extract the table content. The pattern used to extract this is made such that each of Date/Time, incident number, location, nature, and incident ORI are extracted from one of the groups. There is also another pattern that extracts some special nature cases that start with numbers or capitalized words.

#### src/augment.py\
##### create_df()
Takes the extracted incidents from the main file and augments data using padas dataframe functionalities.
Calls geocoder and weather apis to get the side of town and weather code information.
Returns the augmented data in the format specified.

##### rank_dict()
Helper function to rank the locations and incidents based on number of occurrences in a given file.

#### src/geocode.py\
##### GeoCoder
Class to get latitude, longitude for addresses using geopy - Geocodio api; using Geocodio for its 2500 per day free api calls and no hard ratelimits like other apis making it faster to use
Maintains a cache for reducing api calls

##### GeoCoder.update_cache()
Saves the cache dictionary in a pickle

##### GeoCoder.get_latlong()
Calls the api if the address is not already in the cache, updates the cache when api is requested
Adds "Norman, OK" to each location for getting accurate results

##### side()
Given a latlong, returns the side of town of the point based on the direction from center of town. Center of the town is set to East

#### src/weather.py\
##### distance()
Helper function to get distance between two points in a plane.

##### weather_code()
Uses Historical Weather API to get weather codes for latlong and hour of day
Selects 2 points from each side of the town, gets hourly weather code for each location. Later assigns weather code to each latlong in the data based on the nearest response latlong got from the API

#### src/config.py\
Store constants that can be globally accessed

## Tests
#### test_fetch_extract.py\
##### test_download_invalidurl()
Checks if it handles invalid urls without throwing exceptions 

##### test_download_validurl()
Checks if the downloaded file is accessible

##### test_pdfread()
Checks if the downloaded file is not corrupt

##### test_parse()
Checks that information from the file is extracted 

#### test_geo_wether.py\
##### test_distance()
Simple check to see if the distance function is working as expected

##### test_side()
Checks that edge cases are handled for getting the sides

##### test_sides()
Tests weather random points (selected using google maps) are assigned correct sides

<!-- latlong sides -->
![image](https://github.com/CaptainO5/cis6930sp24-assignment2/assets/48147068/f2600bd0-08d6-4cfd-8dec-cb06b73103e9)


##### test_cache()
Tests that cache is initialized correctly on creating a geocoder instance

##### test_latlong()
Tests that empry location gets town's default latlong; this happens because get_latlong() adds "Norman, OK" to each address

##### test_bad_latlong()
Checks that bad locations are also defaulted to the Norman's latlong

## Assumptions

The patterns are created based on some assumptions: Location is assumed to always be capitalized. Nature is assumed to have the first letters of each word capitalized, except for some hardcoded exceptions, which start with MVA, COP, EMS, etc.

Divided the plane into 8 equal parts, keeping the center of the city at origin, side of the town is calculated based on the angle lat-long made with horizontal axis. Center of the town is assumed to be the default location when the location is can not be parsed.
