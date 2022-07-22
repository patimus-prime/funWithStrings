# stringClasses.py
# 21 July 2022
# Patrick Finnerty

# This .py creates the classes, methods we'll use
# during our efforts

# not sure if this counts as a 'standard python library' but v. helpful here
from itertools import permutations as mutator


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
    # Hmmmm...
    # A few optionsl declare a list of this type and feed in mucho strings
    # i.e. with the web page, could save as file and input here; unclear what that looks like
    # for writing, again could need a couple methods to output a list or just a string

    # FIXME: COME BACK LATER AND ADD DESIRABLE METHODS


class anagram(turboString):  # will inherit from turboString
    def __init__(self, initialStr):
        # w. super we inherit all methods and initialize same way
        super().__init__(initialStr)
        # must define below as self, continues pattern:
        self.bankofAnaGraham = []  # a cool band name; also initialize empty list of anagrams

    # methods of anagram --------
    def anagramGenerator(self):
        # a lot here: mutate self.string to everything, mutator outputs characters;
        # each time that happens we join, spacing with nothing (''), and create a string
        # we iterate through those strings with very descriptive iterator 'potentialDuplicateAnagram'
        # then we use set to exclude duplicates, and append.
        # not sure if wise to not have an intermediate object to hold strings, but w/e we'll see

        # not sure if we append or set equal
        self.bankofAnaGrahamA.append(
            set(''.join(potentialDuplicateAnagaram)
                for potentialDuplicateAnagaram in mutator(self.string)))
        # may then set equal and set after, dunno
        self.bankofAnaGrahamB = (
            set(''.join(potentialDuplicateAnagaram)
                for potentialDuplicateAnagaram in mutator(self.string)))


class palindrome(turboString):
    def __init__(self, initialStr):
        super().__init__(initialStr)  # .string for palindrome will be baseString
        self.stringPalindrome = self.mirrorGivenStr(
            self.string)  # THAT'S SO CRAZY LOL

    # methods ----

    # this one returns boolean if some inputted string is a palindrome of this
    # object or what
    def isMyPalindrome(self, potentialPal):
        if (self.stringPalindrome == potentialPal):
            return True
        else:
            return False
