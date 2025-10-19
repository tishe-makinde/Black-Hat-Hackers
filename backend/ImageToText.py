#Libraries

import requests
from pathlib import Path
from PIL import Image
import pytesseract
from numpy.f2py.auxfuncs import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time

import serpapi

#All Search api stuff, P for primary, S for secondary
API_KEY_P = 'AIzaSyBpoBejvPRbMApCnVnym7OuKuTrbtuo8sg'
API_KEY_SP = '59df3bf1cf9f4d4a78173f2411700348c08d660f9cbd6f918f4dbb3513a602b9'
SEARCH_ENGINE_ID_P = '05dc319b892aa4259'
url = 'https://www.googleapis.com/customsearch/v1'

im = Image.open('C:/Users/mofeo/Pictures/Screenshots/Screenshot 2025-10-19 021603.png')
new_size = tuple(4*x for x in im.size)
im = im.resize(new_size, Image.Resampling.LANCZOS)

query = pytesseract.image_to_string(im)

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

response = requests.get(url, params=params_P)
results = response.json()
print(query)

if 'items' in results:
    print("hi1")
    print(results['items'][0]['link'])
else:
    print("hi2")
    client = serpapi.Client(api_key=API_KEY_SP)
    results_SP = client.search(params_SP)
    if 'organic_results' in results_SP:
        print(results_SP["organic_results"][0]["link"])