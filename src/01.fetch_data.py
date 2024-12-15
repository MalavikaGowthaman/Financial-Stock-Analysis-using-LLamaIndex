import os
import urllib.request as request
import zipfile

data_url = "https://github.com/entbappy/Branching-tutorial/raw/master/articles.zip"

def download_file():
    # Download the file
    filename, headers = request.urlretrieve(
        url=data_url,
        filename="articles.zip"
    )
    
    # Unzip the downloaded file using Python's zipfile module
    with zipfile.ZipFile("articles.zip", "r") as zip_ref:
        zip_ref.extractall()  # Extract to the current directory
    
    # Remove the zip file after extraction
    os.remove("articles.zip")

# Run the download and extraction
download_file()
