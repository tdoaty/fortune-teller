import requests
import json
from pprint import pprint

url = "https://api.giphy.com/v1/gifs/search?q=funny+cat&api_key=dc6zaTOxFJmzC"
data = requests.get(url)
gif_data = (data.json())
first_user = gif_data['data'][0]['images']['fixed_height']['url']

#for loop to go through all images
