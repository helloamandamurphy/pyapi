#!/usr/bin/python3
  
import requests

base_url =  "https://pokeapi.co/api/v2/pokemon/"

def api_pull():
    choice= input("What Pokemon would you like a picture of? ")
    poke_url= base_url + choice.lower()
    pokedikt= requests.get(poke_url).json()
    return pokedikt

def api_slice(pokeinfo):
    poke_pic= pokeinfo['sprites']['front_default']
    return poke_pic
    #print(poke_pic)



def main():
    pokeinfo= api_pull()
    api_slice(pokeinfo)

if __name__ == "__main__":
    main()
