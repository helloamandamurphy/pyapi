#!/usr/bin/python3
import requests

## Define NEOW URL 
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def askStart():
    start = input('''
            What would you like as the start date? 
            Enter date in the following format:  YYYY-MM-DD > ''')
    startValue = "start_date=" + start
    return startValue

def askEnd():
    end = input('''
    What would you like as the end date?
    Enter date in the following format: YYYY-MM-DD > ''')
    endValue = "end_date=" + end
    return endValue

def extract(neodata):
    print(neodata["near_earth_objects"])
    #for y in neodata["near_earth_objects"][x]
    #id = y["id"]

def main():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
   
   ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")        

    ## update the date below, if you like
   # startdate = "start_date=2019-11-11"
   # startdate = askStart()

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"
    #enddate = askEnd()

    hazardous = "is_potentially_hazardous_asteroid=True"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + hazardous + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()
    
    extract(neodata)

    ## display NASAs NEOW data
    #print(neodata)

    print(f"Reaper ship id is approaching at mph expected to arrive on date")


if __name__ == "__main__":
    main()

