#!/usr/bin/python3

def askName():
    char_name = input("Which character do you want to know about? (Flash, Batman, Superman) > ")
    return char_name

def askStat():
    char_stat = input("What statistic do you want to know about? (strength, speed, intelligence) > ")
    return char_stat

info =  {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

def main():
    nkey = askName().lower()
    skey = askStat().lower()

    print(f"{nkey.capitalize()}'s {skey} is: {info[nkey][skey]}.")
   # while True: 
    #    namei = int(name)-1
     #   stati = int(stat)-1

      #  try: 
       #     if 0 <= name <= 2:

main()
