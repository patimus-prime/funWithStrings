# typo or test?
# anagram_palyndrom_finder.py
# 21 July 2022
# Patrick Finnerty

# this .py scrapes a webpage given by command line,
# extracts strings/words from that webpage, and reports
# if, per string, there exist palindromes/anagrams elsewhere
# in the webpage, we report 'em to the command line.


# WARNING: REQUIRED FILES
# if missing, may be found at: https://github.com/patimus-prime/funWithStrings
import classDeclarations as C  # get our classes
import getListOfWordsOnPage as W
import textToDF as F
# Now general imports; install via pip if missing
# NOTE: if warning/missing on importing, change py version in VSCode. weird error
from bs4 import BeautifulSoup as BS  # this is BS
import re  # reg ex
import requests as RQ
import pandas as pd
import os
import sys
# -------------------------------------------------------------

# more test cases in textToDF.py
# url = "https://maximum-effort-4dpohzbth-patimus-prime.vercel.app/"

# NORMAL OPERATION:

url = sys.argv[1]  # [0] is this .py

ListOfWordsOnPage = W.getListOfWordsOnPage(url)
df = F.getDataFrameToPrint(ListOfWordsOnPage)

# OUTPUT -----------------
print(df)  # prints df to console, hopefully your screen is big enough

# if you want a csv:
df.to_csv("anagramPalindrome.csv", sep='\t')
print("\n... Also saved anagramPalindrome.csv")
