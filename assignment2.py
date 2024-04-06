import argparse
from src import extract, fetch
from src import augment
import pandas as pd

def main(url_file):
    print('\t'.join(['Day of the Week', 'Time of Day', 'Weather', 'Location Rank', 'Side of Town', 'Incident Rank', 'Nature', 'EMSSTAT']))

    # Read the urls from the file and augment data
    for url in list(pd.read_csv(url_file, header=None, names=['urls']).urls):
        # Download the pdf and get the location
        pdf_path = fetch.download(url)

        # Extract incidents from the downloaded pdf
        incident_list = extract.parse(pdf_path) if pdf_path else [] # Skip the url if there is an error

        if incident_list: # Skip when there is an error parsing
            incident_df = augment.create_df(incident_list)

            for row in incident_df.values:
                print('\t'.join([str(i) for i in row]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls", type=str, required=True, 
                         help="Path to file with Urls")
     
    args = parser.parse_args()
    if args.urls:
        main(args.urls)