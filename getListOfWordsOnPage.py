from bs4 import BeautifulSoup as BS  # this is BS

# NOTE: if warning on importing, change py version in VSCode. weird error
import requests as RQ
# regular expressions
import re
import classDeclarations as C  # get our classes


def getListOfWordsOnPage(url):
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
    # reg ex sets anything not a letter to NOTHING
    for i in range(len(wordList)):
        # tempting to use \W, or \w; but need #s and _ gone
        wordList[i] = re.sub(r'[^a-zA-Z]', '', wordList[i])

    # i notice some one character strings which will throw errors -- so...
    # if a word is below our threshold, it gets set to nothing
    # and then removed in the next step:
    minimumWordLength = 1
    for i in range(len(wordList)):
        if len(wordList[i]) == minimumWordLength:
            wordList[i] = ''  # set those one chars to nothing

    # then remove the NOTHING:
    # remove('') worked on negative test, but failed on others.
    # therefore, from: https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
    wordList = list(filter(None, wordList))

    # EXCELLENT!!!!!!!!!!
    # https://youtu.be/sMqQOGTshak?t=41

    return(wordList)  # BOOM!
