#!/bin/bash

# WARNING: this .sh should be in the project directory
    # if it ain't, need to make the files below more explicit

# NOTE: if can't run, chmod a+x launchFinder.sh
# then ./launchFinder.sh
echo "Welcome!!! This script will print the palindromes and"
echo "anagrams, if they exist, on the passed URL. It will print"
echo "the matched palindromes and anagrams and their index; it's a"
echo "dataframe format printed to shell. By default, a csv is also saved."
echo "Confirm the directory; we are in: "
pwd
echo "The directory should contain ALL related scripts."
echo "This script requires one argument, the url."
echo "Call this script as ./launchFinder [URL here]"
echo "."
echo "."
echo "If the URL you passed results in killed process due to"
echo "excess memory usage, I suggest using my dog's website:"
echo "https://maximum-effort-4dpohzbth-patimus-prime.vercel.app/"
echo "."
echo "."
echo "."
echo "."
echo "... Starting; your url is $1"
echo "."


python3 anagram_palyndrom_finder.py $1