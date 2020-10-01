#!/usr/bin/python3
  
import requests
import wget

base_url =  "https://pokeapi.co/api/v2/pokemon/"

#ASSIGNED
def api_pull():
    choice= input("What Pokemon would you like a picture of? ")
    poke_url= base_url + choice.lower()
    pokedikt= requests.get(poke_url).json()
    return pokedikt

#ASSIGNED
def api_slice(pokeinfo):
    poke_pic= pokeinfo['sprites']['front_default']
    return poke_pic
    #print(poke_pic)

#EXTRA
def wget_pic(imagelink):
    wget.download(imagelink, '/home/student/static/')

def main():
    wget_pic(api_slice(api_pull))

if __name__ == "__main__":
    main()
