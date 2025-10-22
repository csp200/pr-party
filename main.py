#!/usr/bin/env python3
 
import greetings

# define a function that calls your library definition below:
def lee_hello():
    greetings.lee.hello()

# Greeting for tyson.py
def tyson_hello():
    greetings.tyson.hello()

# add a call to your function in main, below the heading output: 
def main():
    print("Fall 2025 CSP 200 PR Yearbook")
    print("=============================")
    lee_hello()
    print()
    print("=============================")
    tyson_hello()
# don't touch this!
if __name__ == "__main__":
    main()
