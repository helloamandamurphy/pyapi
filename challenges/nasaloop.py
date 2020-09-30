#!/usr/bin/python3

import requests

urls = list()

def main():
    mars = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY").json()

   # for images in mars["photos"]:
      #  image = images["img_src"]
     #   urls.append(resp)
    #print(urls)
    
    for images in mars["photos"]:
        print(f"Rover: {images['rover']['name']}")
        print(f"Date: {images['earth_date']}")
if __name__ == "__main__":
    main()
