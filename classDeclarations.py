# classDeclarations.py
# 21 July 2022
# Patrick Finnerty

# This .py creates the classes, methods we'll use
# during our efforts

# not sure if this counts as a 'standard python library' but v. helpful here
from itertools import permutations as mutator


###############
# HUGE WARNING: MAY NEED TO DO TOUPPER() or tolower() below on input strings
# depending on methods/how python treats the capitals/what's desirable
# for now forging ahead without, but a note that this is a consideration
###############
class turboString:
    def __init__(self, initialStr):
        # beware maybe need something to account for if already declared?
        self.string = initialStr

    # methods for this object -------

    def appendSelf(self, newStr):  # has initialStr already available
        self.string += newStr  # should append newStr to that string

    def removeSubStr(self, subStr):
        # find subStr in self.string, replace w. nada
        self.string = str.replace(self.string, subStr, "")

    # 2 methods for mirroring, not sure exactly what's desired: --------

    # warning! this one alters base string to reverse;
    # see palindrome declaration for safer option to reverse
    # just putting this in for the sake of thoroughness
    def mirrorSelf(self):
        self.string = self.string[::-1]  # slices backwards, reverse
        # a reminder to self: [XYZ] X is start index, Y end index, Z iterator

    def mirrorGivenStr(self, givenStr):  # may not even need self I don't think
        givenStr = givenStr[::-1]
        return givenStr

    # I/O operations; I suspect unlikely to be used during this project: -------
    def readInFileAsString(self, filePath):
        # this is a pretty sus operation, but here it is:
        temp = open(filePath, "r")
        self.string = temp
        temp.close()

    def writeStringAsFile(self, filePath):
        temp = open(filePath, "w")
        temp.write(self.string)
        temp.close()


class anagram(turboString):  # will inherit from turboString
    def __init__(self, initialStr):
        # w. super we inherit all methods and initialize same way
        super().__init__(initialStr)
        self.bankofAnaGraham = []  # a cool band name; also initialize empty list of anagrams

    # methods of anagram --------

    def anagramGenerator(self):
        # a lot here: mutate self.string to everything, mutator outputs characters;
        # each time that happens we join, spacing with nothing (''), and create a string
        # we iterate through those strings with very descriptive iterator 'potentialDuplicateAnagram'
        # then we use set to exclude duplicates. AND THEN...
        # we call list on the set object to get back to a list; set has no
        # useful attributes, just a nice way to get the unique anagrams, no dupes
        # .append and just = set aren't good. don't do that. go back to list

        self.bankofAnaGraham = list(set(''.join(potentialDuplicateAnagaram)
                                        for potentialDuplicateAnagaram in mutator(self.string)))  # compiler is crazy no need for \


class palindrome(turboString):
    def __init__(self, initialStr):
        super().__init__(initialStr)  # .string for palindrome will be baseString
        self.isPalindrome = self.isMyPalindrome(initialStr)
        # this returns the reverse of the input string...
        # but that's all it is.
        # rather we should have an attrbiute to hold T/F palindrome;
        # the string will already be a palindrome.
        # self.stringPalindrome = self.mirrorGivenStr(
        #    self.string)  # THAT'S SO CRAZY LOL

    # methods ----

    # this one returns boolean if some inputted string is a palindrome of this
    # object or what
    def isMyPalindrome(self, potentialPal):
        if (self.string == self.mirrorGivenStr(potentialPal)):
            return True
        else:
            return False
