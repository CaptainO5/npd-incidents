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


## How to run tests


`pipenv run python -m pytest`


<!-- video -->



## Functions
#### assignment2.py \

This is the starting point of the program, which parses the command-line input URL File and send it to main

##### main()
Iterate over the urls, download the files and call augment data funciton before printing it to the stdout.
Prints the header once, prints the augmented data in the order of their appearance.

#### src/fetch.py \
##### download()
Uses the urlib library to download the given pdf and returns the location accessible to the extractor.


#### src/extract.py \
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

#### src/config.py\
Store constants that can be globally accessed

## Tests
#### test_fetch_extract.py\
##### test_download_invalidurl()

##### test_download_validurl()

##### test_pdfread()

##### test_parse()

#### test_geo_wether.py\
##### test_distance()

##### test_side()

##### test_sides()

##### test_cache()

##### test_latlong()

##### test_bad_latlong()

## Assumptions

The patterns are created based on some assumptions: Location is assumed to always be capitalized. Nature is assumed to have the first letters of each word capitalized, except for some hardcoded exceptions, which start with MVA, COP, EMS, etc.

Divided the plane into 8 equal parts, keeping the center of the city at origin, side of the town is calculated based on the angle lat-long made with horizontal axis. Center of the town is assumed to be the default location when the location is can not be parsed.
