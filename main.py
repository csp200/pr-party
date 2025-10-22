#!/usr/bin/env python3
 
import greetings
from greetings.saswati import greet_saswati


# define a function that calls your library definition below:
def lee_hello():
    greetings.lee.hello()
def cgarcia_hello():
    greetings.cgarcia4.my_name()
def adrian_hello():
    greetings.adrian.hello()
    
def call_saswati_greeting():
    greet_saswati()


def logan_hello():
    greetings.logan.hello()
def Jesus_hello():
    greetings.jesusq.Jesus_hello()
def adore1_hello():
    greetings.adore1.adore1_hello()

def salman_hello():
    greetings.salman.hello()
# Greeting for tyson.py
def tyson_hello():
    greetings.tyson.hello()

def ben_hello():
    greetings.ben.hello()
# add a call to your function in main, below the heading output: 
def main():
    print("Fall 2025 CSP 200 PR Yearbook")
    print("=============================")
    lee_hello()
    ben_hello()
    cgarcia_hello()
    adrian_hello()
    logan_hello()

    call_saswati_greeting()

    
    Jesus_hello()
    adore1_hello()

    salman_hello()

    print()
    print()
    tyson_hello()
# don't touch this!
if __name__ == "__main__":
    main()
