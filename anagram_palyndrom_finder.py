# typo or test?
# anagram_palyndrom_finder.py
# 21 July 2022
# Patrick Finnerty

# WARNING: REQUIRED FILE "classDeclarations.py"
# if missing, may be found at: https://github.com/patimus-prime/funWithStrings
import classDeclarations as C  # get our classes

# WARNING: Unusual dependency (to me)
# may install via pip; I used: pip3 install bs4
# python documentation recommends pip install beautifulsoup4
# whatever works so that the below line doesn't throw errors:
# BS unlikely necessary but nice to be explicit
from bs4 import BeautifulSoup as BS

# let's do some testing of the classes:
ts = C.turboString("Magic")

# this works; C is now just the only bank
# for i in range(len(a.bankofAnaGrahamC)):
# print(i,"is",a.bankofAnaGrahamC[i])
