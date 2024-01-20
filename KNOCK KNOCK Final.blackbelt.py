# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 19:13:10 2024

@author: Isaiah
"""
answer1 = ["who is there", "who is there?", "who's there?", "who's there", "whos there", "whos there?"]
answer2 = ["letuce who?", "letuce who", "lettuce who?", "lettuce who"]
validAns1 = False
validAns2 = False

firstName = input("Hello, what is your name? ")
print(f"Hi {firstName}, how about I share a joke with you? ")

response = input("Y/N ")
response = response.upper()
if response[0] == "Y":
    print("okay let's begin. ")

    question1 = input("knock knock: ")
    question1 = question1.lower()
    for x in answer1:
        if question1 == x:
            validAns1 = True
            break
    if validAns1 == True:          
        question2 = input("lettuce: ")
        question2 = question2.lower()
        for x in answer2:
            if question2 == x:
                validAns2 = True
                break
        if validAns2 == True:  
            print("lettuce in, it's freezing out here! ")
        else:
            print("you were suppose to say 'lettuce who? ' ")
    else:
        print("you were meant to say 'who's there?' ")
else: 
    print("okay no joke for now! maybe another time ")
    
    
