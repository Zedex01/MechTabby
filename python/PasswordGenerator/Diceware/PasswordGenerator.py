import os
import pdfplumber
import promptlib
import pandas as pd

import random as r

import csv

def GetFile(): #Prompts user for a file
    prompter = promptlib.Files();
    _file = prompter.file();
    return _file;

def GenerateDiceRoll():
    diceRoll = []
    
    for i in range(0,5):
        diceRoll.append(r.randint(1,6))
        
    return diceRoll

def GetWordList():
    with open('EFFWordList.csv', newline='') as f:
        wordList = list(csv.reader(f))

    return wordList
    
#Settings==================================

#Mandantory===
numberOfWords = 4
numberOfPasswords = 100

#==========================================
    
#Get the word list from file and convert to dictionary
wordList = dict(GetWordList())

for _ in range(numberOfPasswords):

    password = []
    
    for _ in range(numberOfWords):
        roll = GenerateDiceRoll() #Generate 6 dice rolls
        roll = "".join(str(n) for n in roll) #Convert list of rolls to string
        word = wordList.get(roll) #Get Word from diceware table
        word = (word[0]).upper() + word[1:]#Captilize first letter:
        password.append(word) #Append the word to the password
    print("================================")
    for word in password:
        print(word,end=" ")
    print("")
    password = "".join(password) #Convert list of words into single string
    print(password)