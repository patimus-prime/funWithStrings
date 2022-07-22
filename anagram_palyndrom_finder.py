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

# Now general imports; install via pip if missing
# NOTE: if warning/missing on importing, change py version in VSCode. weird error
from bs4 import BeautifulSoup as BS  # this is BS
import re  # reg ex
import requests as RQ
import pandas as pd
# -------------------------------------------------------------


def fnPalindrome(wordToExamine, df):
    tempPalindromeList = []  # [ tuple() ] # reinitialize each time this function is called
    # create palindrome from our word we examining
    tempPalObject = C.palindrome(wordToExamine)
    # now, with this wordToExamine, cross-ref with EVERY OTHER WORD in the dataframe;
    # and if we come across one that's a palindrome, add to the list
    for index, row in df.iterrows():
        word = row['words']
        if(tempPalObject.isMyPalindrome(word) == True):
            tempPalindromeList.append([word, index])  # and word.index?
    # for word in df['words']:
    #     if(tempPalObject.isMyPalindrome(word) == True):
    #         tempPalindromeList.append(word) #and word.index?
    return(tempPalindromeList)


# use the site i'm developing as a negative case
# NEGATIVE TEST, NO ANA/PALS:
# url = "https://maximum-effort-eif1qd0c4-patimus-prime.vercel.app/"
# POSITIVE TEST, ANA:
# POSITIVE TEST, PALS:
url = "https://examples.yourdictionary.com/palindrome-examples.html"
# POSITIVE TEST, BOTH:


# url = "https://maximum-effort-eif1qd0c4-patimus-prime.vercel.app/"
#url = "https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python"


#url = "https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings"
ListOfWordsOnPage = W.getListOfWordsOnPage(url)

# for my next trick, we'll create a dataframe to check for the rest of things.
# dfToPrint = getFinalDF(ListOfWordsOnPage)
df = pd.DataFrame(ListOfWordsOnPage)
df = df.rename(columns={0: "words"})  # just dealing w. default column behavior
# p = "racecar"
# lp = fnPalindrome(p)
# now we'll iterate through that first col and find stuff.

# df['anagram_list'] = df['words'].apply(lambda x: fnAnagrams(x, df))

df['palindrome_list'] = df['words'].apply(lambda x: fnPalindrome(x, df))
# df['TPSA'] = df['ROMol'].apply(lambda x: D.TPSA(x, includeSandP = True))
df.to_csv("test.csv", sep='\t')

# result = [f(x) for x in df['col']]

# def fnAnagrams(wordToExamine):
# we receive a regular string, one at a time
# we'll return a list of words that are anagrams and their matches


# this works; C is now just the only bank
# for i in range(len(a.bankofAnaGrahamC)):
# print(i,"is",a.bankofAnaGrahamC[i])
