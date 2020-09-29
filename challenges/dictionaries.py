#!/usr/bin/python3
import argparse

hero =  {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

#What I had (not correct)
#ap = argparse.ArgumentParser()
#ap.add_argument('name', "-n", "--name", required=True, 
        #help="name of the hero")
#ap.add_argument('stat', "-s", "--stat", required=True,
        #help="stat of the hero")
#args = vars(ap.parse_args())

#print(f"{args.name}'s {args.stat} is: .")

#Based off Didi's solution shared in the class.
def printHero(heroInput, statInput):
    print(f"{heroInput.capitalize()'s  {statInput} is: {str(hero[heroInput][statInput])}"

answer= ' ' 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Superhero Stats")
    parser.add_argument('-hero', choices=heros.keys(), metavar='HERO', default='flash', help="Pick a hero (Flash, Batman, Superman)")
    parser.add_argument('-stat', choices=heros['flash'].keys(), metavar='STAT', default='speed', help="Pick a stat (speed, intelligence, strength)")

args = parser.parse_args()
printHero(args.hero, args.stat)
