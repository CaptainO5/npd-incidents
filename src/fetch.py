import urllib
from urllib import request
import os
import sys

def download(url, here=False):
    try:
        if here:
            filename = url.split('/')[-1]
            file_path = os.path.join('./', filename)

            # Download and store the file at the given file_path
            request.urlretrieve(url, file_path)
        else:
            # Download and the store the pdf in a temporary local location
            file_path, _ = request.urlretrieve(url)
        return file_path
    except urllib.error.HTTPError as e:
        print(f"Can not download the pdf: {e}", file=sys.stderr)
    except ValueError:
        print(f"Download Error: Bad URL - {url}", file=sys.stderr)
    
    return None