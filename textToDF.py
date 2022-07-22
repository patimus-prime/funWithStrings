# contains functions for parsing text from website,
# and constructing the dataframe that will be returned

import classDeclarations as C  # get our classes
import getListOfWordsOnPage as W
import textToDF as F
# Now general imports; install via pip if missing
# NOTE: if warning/missing on importing, change py version in VSCode. weird error
from bs4 import BeautifulSoup as BS  # this is BS
import re  # reg ex
import requests as RQ
import pandas as pd

# TEST CASES: -----------------


# use the site i'm developing as a negative case
# NEGATIVE TEST, NO ANA/PALS:
# url = "https://maximum-effort-eif1qd0c4-patimus-prime.vercel.app/"

# POSITIVE TEST, ANA:
# WARNING: BOTH USE TOO MUCH MEMORY, DID NOT USE
# url = "https://literarydevices.net/anagram/"
# url = "https://www.softschools.com/examples/grammar/anagrams_examples/222/"

# POSITIVE TEST, PALS:
#url = "https://examples.yourdictionary.com/palindrome-examples.html"

# POSITIVE TEST, BOTH:
# url = "https://maximum-effort-4dpohzbth-patimus-prime.vercel.app/"


# ------------------------------


def fnPalindrome(wordToExamine, df):
    tempPalindromeList = []  # [ tuple() ] # reinitialize each time this function is called
    # create palindrome from our word we examining
    tempPalObject = C.palindrome(wordToExamine)
    # now, with this wordToExamine, cross-ref with EVERY OTHER WORD in the dataframe;
    # and if we come across one that's a palindrome, add to the list

    # BIG WARNING: will report itself if it's a palindrome, along with others
    for index, row in df.iterrows():
        word = row['words']
        if(tempPalObject.isMyPalindrome(word) == True):
            tempPalindromeList.append([word, index])  # and word.index?

    return(tempPalindromeList)


def fnAnagram(wordToExamine, df):
    tempAnagramList = []
    tempAnaObject = C.anagram(wordToExamine)
    tempAnaObject.anagramGenerator()
    for index, row in df.iterrows():
        word = row['words']
        if ((word in tempAnaObject.bankofAnaGraham) and word != wordToExamine):
            tempAnagramList.append([word, index])
    return(tempAnagramList)


def fnCheckIfEmptyList(xList):
    if (len(xList) == 0):
        return False
    else:
        return True


def getDataFrameToPrint(ListOfWordsOnPage):
    df = pd.DataFrame(ListOfWordsOnPage)
    # just dealing w. default column behavior
    df = df.rename(columns={0: "words"})

    # generate features to print -----------

    df['palindrome_list'] = df['words'].apply(lambda x: fnPalindrome(x, df))
    df['anagram_list'] = df['words'].apply(lambda x: fnAnagram(x, df))
    df['has_palindrome'] = df['palindrome_list'].apply(
        lambda x: fnCheckIfEmptyList(x))
    df['has_anagram'] = df['anagram_list'].apply(
        lambda x: fnCheckIfEmptyList(x))

    return df
