#!/usr/bin/python3

import threading
import time

def print_name():
    name = "Persephone".upper()
    name_list = list()
    name_list[:0]=name
    
    for letter in name_list: 
        print(letter),

def slowdown():
    time.sleep(1)

def main():
    print("Let's try this out:")
    t1 = threading.Thread(target=print_name, name='letters')
    t2 = threading.Thread(target=slowdown, name='sleeper')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
