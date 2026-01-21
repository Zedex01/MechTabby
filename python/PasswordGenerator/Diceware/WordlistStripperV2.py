import os
import promptlib
import pandas as pd


def GetFile(): #Prompts user for a file
    prompter = promptlib.Files();
    _file = prompter.file();
    return _file;
    
    
    
#Setup============================================
ignore = "Diceware.com Dice-Indexed Passphrase Word List"


wordList = [["Dice", "Word"]]

#=================================================    
    
    

#Get this scripts location
absolutePath = os.path.dirname(__file__)

file = GetFile()
#_file = os.path.join(file, _file) #File name

with open(file) as f:
    for line in f:        
        line = line.strip().split("\t")
        wordList.append([line[0], line[1]])
    
df = pd.DataFrame(wordList)
print(df)

wordCnt = len(wordList)
amnt = wordCnt**4
print(f"Total Words: {wordCnt} | Max combos: {amnt}")

#Write to output File
df.to_csv('EFFWordList.csv', index=False)

