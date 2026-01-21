import os
import pdfplumber
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


with pdfplumber.open(file) as pdf:
    for i, page in enumerate(pdf.pages):
        
        #Skip the last page
        if i+1 > 36: 
            continue

        pageContent = page.extract_text()
        pageContent = pageContent.split("\n")
        
        for line in pageContent:
            
            #ignore unimportant lines
            if (line[:4] == "Page") or (line == ignore):
                continue
                
            
            phrases = line.split(" ")
            
            for i in range (0, 7, 2):
                wordList.append([phrases[i],phrases[i+1]])



    
df = pd.DataFrame(wordList)
print(df)

wordCnt = len(wordList)
amnt = wordCnt**4
print(f"Total Words: {wordCnt} | Max combos: {amnt}")

#Write to output File
df.to_csv('WordList.csv', index=False)

