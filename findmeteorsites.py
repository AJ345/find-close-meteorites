import requests
import math 
meteor_response = requests.get("https://xkcd.com/353/")
print(meteor_response.text)
