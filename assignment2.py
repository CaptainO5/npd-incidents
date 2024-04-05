import argparse
from src import extract, fetch
from src import augment
import pandas as pd

def main(url_file):
    # Read the urls from the 
    for url in list(pd.read_csv(url_file, header=None, names=['urls']).urls):
        # Download the pdf and get the location
        pdf_path = fetch.download(url)

        # Extract incidents from the downloaded pdf
        incident_list = extract.parse(pdf_path) if pdf_path else [] # Skip the url if there is an error

        if incident_list: # Skip when there is an error parsing
            incident_df = augment.create_df(incident_list)

            print(incident_df)
        break

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls", type=str, required=True, 
                         help="Path to file with Urls")
     
    args = parser.parse_args()
    if args.urls:
        main(args.urls)