#!/usr/bin/env python3
 
import greetings
from greetings.suproteek import greet_suproteek

# define a function that calls your library definition below:
def lee_hello():
    greetings.lee.hello()
    
def call_suproteek_greeting():
    greet_suproteek()


def jdoe_hello():
    greetings.jdoe.jdoe_hello()

# add a call to your function in main, below the heading output: 
def main():
    print("Fall 2025 CSP 200 PR Yearbook")
    print("=============================")
    
    lee_hello()
    jdoe_hello()

    call_suproteek_greeting()


# don't touch this!
if __name__ == "__main__":
    main()
