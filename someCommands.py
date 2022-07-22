# coding: utf-8
# typo or test?
# anagram_palyndrom_finder.py
# 21 July 2022
# Patrick Finnerty

# this .py scrapes a webpage given by command line,
# extracts strings/words from that webpage, and reports
# if, per string, there exist palindromes/anagrams elsewhere
# in the webpage, we report 'em to the command line.


# WARNING: REQUIRED FILE "classDeclarations.py"
# if missing, may be found at: https://github.com/patimus-prime/funWithStrings
import classDeclarations as C  # get our classes

# WARNING: Unusual dependency (to me)
# may install via pip; I used: pip3 install bs4
# python documentation recommends pip install beautifulsoup4
# whatever works so that the below line doesn't throw errors:
# BS unnecessary but nice to be explicit
from bs4 import BeautifulSoup as BS  # this is BS

# NOTE: if warning on importing, change py version in VSCode. weird error
import requests as RQ

# -------------------------------------------------------------

# use the site i'm developing as a negative case
# NEGATIVE TEST, NO ANA/PALS: "https://maximum-effort-eif1qd0c4-patimus-prime.vercel.app/"
# POSITIVE TEST, ANA:
# POSITIVE TEST, PALS:
# POSITIVE TEST, BOTH:

url = "https://maximum-effort-eif1qd0c4-patimus-prime.vercel.app/"
webPage = RQ.get(url)  # 2nd arg is option for fake headers if necessary

# uses default python parser, may change if you want
soup = BS(webPage.content, 'html.parser')

# almost same as .text; but this lets us enforce a delimiter
strToParse = soup.get_text(" ")
strToParse.lower
print(strToParse.lower)
strToParse
strToParse.lower()
strToparse
strToParse
strToParse = strToParse.lower()
strToParse
wordList = strToParse.split()
wordList
import re
re.sub(r'\W+','',strToParse)
strToParse
re.sub(r'\W+', '',strToParse)
re.sub(r'\W+', ',strToParse)
re.sub(r'\W+', ' ', strToParse)
# shit... so let's instead...
wordList = strToParse.split()
wordList
for i in range(len(wordList)):
    re.sub(r'\W+','',wordList[i])
    
wordList
for i in range(len(wordList)):
    wordList = re.sub(r'\W+','',wordList[i])
wordList
wordList = strToParse.split()
for i in range(len(wordList)):
    wordList = re.sub(r'\W+','',wordList[i])
    
strToParse
wordList = strToParse.split()
wordList
for i in range(len(wordList)):
    re.sub(r'\W+','',wordList[i])
    
wordList
wordList[0]
for i in range(len(wordList)):
   wordList[i] =  re.sub(r'\W+','',wordList[i])
wordList
wordList.remove()
wordList.remove('')
wordList
