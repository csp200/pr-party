#!/usr/bin/env python3
 
import greetings
from greetings.saswati import greet_saswati


# define a function that calls your library definition below:
def lee_hello():
    greetings.lee.hello()
    
def call_saswati_greeting():
    greet_saswati()


# add a call to your function in main, below the heading output: 
def main():
    print("Fall 2025 CSP 200 PR Yearbook")
    print("=============================")
    
    lee_hello()
    call_saswati_greeting()

    

# don't touch this!
if __name__ == "__main__":
    main()
