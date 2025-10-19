#Libraries

import requests
from pathlib import Path
from PIL import Image
import pytesseract

import serpapi

#All Search api stuff, P for primary, SP for SerpAPI
API_KEY_P = 'AIzaSyBpoBejvPRbMApCnVnym7OuKuTrbtuo8sg'
API_KEY_SP = '59df3bf1cf9f4d4a78173f2411700348c08d660f9cbd6f918f4dbb3513a602b9'
SEARCH_ENGINE_ID_P = '05dc319b892aa4259'
url = 'https://www.googleapis.com/customsearch/v1' #Google Search link

#Resize Images to increase their size and make it easier to read by pytesseract
im = Image.open('C:/Users/mofeo/Pictures/Screenshots/Screenshot 2025-10-19 021603.png') #Actual Image file itself
new_size = tuple(4*x for x in im.size)
im = im.resize(new_size, Image.Resampling.LANCZOS)

#Text detected by pytesseract
query = pytesseract.image_to_string(im)

#Params to send to the API
params_P = {
    'q': query,
    'key': API_KEY_P,
    'cx': SEARCH_ENGINE_ID_P
}

params_SP = {
  "q": query,
  "google_domain": "google.com",
  "api_key": "59df3bf1cf9f4d4a78173f2411700348c08d660f9cbd6f918f4dbb3513a602b9"
}

#Returned json of metadata retrieved
response = requests.get(url, params=params_P)
results = response.json()
#print(query)

#If the restricted social media search finds links then use that, if not then use the whole of Google
def finalURL():
    if 'items' in results:
        return results['items'][0]['link']#Print top link
    else:
        #Use serpAPI here instead of Google's API to search unrestricted Google
        client = serpapi.Client(api_key=API_KEY_SP)
        results_SP = client.search(params_SP)
        if 'organic_results' in results_SP: #Same principle as previous if statement without another else
            return results_SP["organic_results"][0]["link"] # Return top link
        else:
            return "No Results" #If nothing relating to the image can be found