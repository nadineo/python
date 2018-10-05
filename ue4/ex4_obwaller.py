##################################################
# IINI4014 Python for programmers (2018 HØST)
# Nadine Obwaller
# Exercise 3: File I/O and text processing
##################################################
import os
import re
import sys
from collections import Counter

## Part 1 - Listing files

def getfilelist(path):
    files_in_dir = []
    for root, dirs, files in os.walk(path):  
        for file in files:
            if file.endswith(".txt"):
            	#append every .txt file with path to the list
                files_in_dir.append(os.path.join(root, file))
    files_in_dir.sort()
    return files_in_dir


## Part 2 - Dictionary of word frequencies
def getwordfreqs(file):
    with open(file,'r') as f:
    	#read file and convert letters to lower-case
        words = re.findall(r'\w+', f.read().lower())
    #get frequencies of all words
    word_freq = Counter(words)
    dictionary = dict(word_freq)
    return dictionary


## Part 3 - Most frequent words common to all dictionaries
def getcommonwords(dictionaries):
    common_words = {}

    #check if dictionaries have entries
    if len(dictionaries) > 0:
        #get 10 common words in the first dictionary 
        common_words = set(Counter(dict(Counter(dictionaries[0]).most_common(10))).keys())
        #build intersection among all common 10 words in all dictionaries
        for words in dictionaries:
            common_words &= set(Counter(dict(Counter(words).most_common(10))).keys())

    return list(common_words)
    
    
dicts = []
# Get the list of files
for f in getfilelist(sys.argv[1]):
    # Get word frequencies
    dicts.append(getwordfreqs(f))

# Get common words
for w in getcommonwords(dicts):
    print(w)
