"""

We know that every website contains a main image and a main description.
So here is the python code to extract them using Beautiful Soup.

url=== Contains the URL of the page from where you want to scrap
source=== The base URL. (Eg:: https://www.facebook.com) We need this because sometimes the relative URL is given in
the source page for the image field.

"""
import requests
from bs4 import BeautifulSoup

def get_meta_info(url,source):
    response = requests.get(url,timeout=10, headers={"User-Agent": "Python"})
    soup = BeautifulSoup(response.text, "html.parser")
    try:
        image_link = soup.findAll("meta", {"property": "og:image"})[0].attrs['content']   
    except Exception:
        try:
            image_link = soup.findAll("meta", {"name": "twitter:image"})[0].attrs['content']
        except Exception:
            image_link=None       
    if (image_link is not None) and ('http' not in image_link):
        image_link=source+image_link
    try:
        description = soup.findAll("meta", {"property": "og:description"})[0].attrs['content']
    except Exception:
        try:
            description = soup.findAll("meta", {"name": "twitter:description"})[0].attrs['content']
        except Exception:
            description=None   
    return image_link, description

