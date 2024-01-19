# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 19:13:10 2024

@author: chibuike
"""

firstname = input("Please what is your name? ")
print(f"Hi {firstname}, how about I share a joke with you? ")

response = input("Y/N ")
response = response.upper()
if response[0] == "Y":
    print("okay let's begin. ")

    question1 = input("knock knock: ")
    question1 = question1.lower()
    if question1 == "who's there?":
        question2 = input("lettuce: ")
        question2 = question2.lower()
        if question2 == "lettuce who?":
            print("lettuce in, it's freezing out here! ")
        else:
            print("you were suppose to say 'lettuce who? ' ")
    else:
        print("you were meant to say 'who's there?' ")
        
else: 
    print("okay no joke for now! maybe another time ")
    
    