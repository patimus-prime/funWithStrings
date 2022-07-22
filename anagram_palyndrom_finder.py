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
# regular expressions
import re
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

# lower all capitals, make sure our stuff picks up on everything:
# does alter data a little I guess; one can look at indeces later to find source word
# or declare an extra object 'unaltered str' and then cross-ref with strToParse
strToParse = strToParse.lower()
# print(strToParse) # PERFECT!

# we must now add each word, delimited by a space, to a list, which will then be fed into
# another fn.
wordList = strToParse.split()

# this preserves "--" though and some punctuation that'll mess our stuff up,
# so to remove, iterate through words and if there's punctuation, take it out:
# reg ex sets anything not an alphanumeric to NOTHING
for i in range(len(wordList)):
    wordList[i] = re.sub(r'\W+', '', wordList[i])

# then remove the NOTHING:
wordList.remove('')

# EXCELLENT!!!!!!!!!!
# https://youtu.be/sMqQOGTshak?t=41


# need to separate out \w for words if that's enough, but also split by " " and capitals,
# probably also punctuation. After that we'll have a nice str or list, however we do it.


# this works; C is now just the only bank
# for i in range(len(a.bankofAnaGrahamC)):
# print(i,"is",a.bankofAnaGrahamC[i])
