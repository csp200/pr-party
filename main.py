#!/usr/bin/env python3
 
import greetings
from greetings.saswati import greet_saswati


# define a function that calls your library definition below:
def lee_hello():
    greetings.lee.hello()
def cgarcia_hello():
    greetings.cgarcia4.my_name()
    
def call_saswati_greeting():
    greet_saswati()


def logan_hello():
    greetings.logan.hello()
def Jesus_hello():
    greetings.jesusq.Jesus_hello()
# add a call to your function in main, below the heading output: 
def main():
    print("Fall 2025 CSP 200 PR Yearbook")
    print("=============================")
    
    lee_hello()
    cgarcia_hello()
    logan_hello()
    jdoe_hello()

    call_suproteek_greeting()
    call_saswati_greeting()

    
    Jesus_hello()

# don't touch this!
if __name__ == "__main__":
    main()
