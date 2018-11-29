#! python3
# Exam.py - xxxxxx

'''
Brief structure:
    - Read text from file1
    - Build histogram of the words from file1
    - Read text from file2
    - Analyze the text from file2
'''

import os
import pprint


# Characters we would like to strip off, like dots and commas
stripCharacters = '.,'

#######################################################################
# Objective 4: Percentage of different words, use FirstTextFile for this
#######################################################################

# Relative folder with text files
textFileFolder = '.'                                # Current folder
absPath = os.path.abspath(textFileFolder)
fileName = 'FirstTextFile.txt'                      # Use first file as reference

# open the first text file, read the text
# List of words
words = []

file = open(os.path.join(absPath, fileName), 'r')
fileContent = file.read()
parts = fileContent.split()                         # split the text in parts, divided by white space
for part in parts:                                  # iterate on parts
    part = part.strip(stripCharacters)              # remove dots and commas from the ends
    if part.isalpha():
        words.append(part.lower())                  # build list of lower case words, letters only
file.close()

numberOfWords = len(words)

# Create a dictionary with each word and the usage
wordDict = {}                                       # create empty dictionary
for word in words:                                  # for each word in words list
    wordDict.setdefault(word, 0)                     # if word is not a key in the dictionary, create it with zero as value
    wordDict[word] += 1                              # count it

# Replace count of word with percentage
for word in wordDict:
    number = wordDict.get(word, 0)
    percentage = number / numberOfWords * 100.0
    wordDict[word] = percentage

# Then analyse SecondTextFile
fileName = 'SecondTextFile.txt'

words2 = []

file = open(os.path.join(absPath, fileName), 'r')
fileContent = file.read()
parts = fileContent.split()                         # split the text in parts, divided by white space
for part in parts:                                  # iterate on parts
    part = part.strip(stripCharacters)              # remove dots and commas from the ends
    if part.isalpha():
        words2.append(part.lower())                 # build list of lower case words, letters only
file.close()

numberOfWords2 = len(words2)

#########################################################
# Objective 2&3: Percentage of easy words/difficult words
#########################################################

# Set arbitrary limits for easy and difficult
easyLimit = 0.5                                     # A word that has a usage of more than easyLimit percent in a reference text is easy
difficultLimit = 0.01                               # A word that has a usage of less than difficultLimit percent in a reference text is difficult


# First, do this for all words in words2, also duplicates
easyWordCount = 0
difficultWordCount = 0
for word in words2:
    referencePercentage = wordDict.get(word, 0)      # Get the reference value from the dictionary
    if referencePercentage > easyLimit:
        easyWordCount += 1                          # This is an easy word
    elif referencePercentage < difficultLimit:
        difficultWordCount += 1                     # This is a difficult word

easyWordPercentage = easyWordCount / numberOfWords2 * 100
difficultWordPercentage = difficultWordCount / numberOfWords2 * 100

# Round off with int in the print statements
print('Analyse SecondTextFile.txt:')
print(str(int(easyWordPercentage)) + ' % of all words are easy.')
print(str(int(difficultWordPercentage)) + ' % of all words are difficult.')
print(str(int(100.0 - easyWordPercentage - difficultWordPercentage)) + ' % of all words are of intermediate complexity.')
print()

# Then do it for unique words
uniqueWords = []                                     # Define list of unique words
easyWordCount = 0
difficultWordCount = 0

for word in words2:
    if word not in uniqueWords:
        uniqueWords.append(word)                    # Build list of unique words
for word in uniqueWords:
    referencePercentage = wordDict.get(word, 0)      # Get the reference value from the dictionary
    if referencePercentage > easyLimit:
        easyWordCount += 1                          # This is an easy word
    elif referencePercentage < difficultLimit:
        difficultWordCount += 1                     # This is a difficult word

easyWordPercentage = easyWordCount / len(uniqueWords) * 100
difficultWordPercentage = difficultWordCount / len(uniqueWords) * 100

print(str(int(easyWordPercentage)) + ' % of the unique words are easy.')
print(str(int(difficultWordPercentage)) + ' % of the unique words are difficult.')
print(str(int(100.0 - easyWordPercentage - difficultWordPercentage)) + ' % of the unique words are of intermediate complexity.')
print()

#######################################
# Objective 1: Sentence length in words
#######################################

# Reuse fileContent from above:
sentences = fileContent.split('.')                  # List of sentences from SecondTextFile
numberOfSentences = len(sentences)

totalNumberOfWordsInAllSentences = 0
for sentence in sentences:
    wordsInSentence = sentence.split()              # Split the sentence in words
    numberOfWordsInSentence = len(wordsInSentence)
    totalNumberOfWordsInAllSentences += numberOfWordsInSentence  # This is probably the same as numberOfWords2 above, but anyway...
    if numberOfWordsInSentence == 0:                # This is not a sentence
        numberOfSentences -= 1

averageSentenceLength = totalNumberOfWordsInAllSentences / numberOfSentences
print('The average sentence length is: ' + str(int(averageSentenceLength)) + ' words.')

################################################
# Objective 5: Number of sentences per paragraph
################################################
# Note: If the order of objective 1 and 5 is switched, the code can be simplified. But that will be another day...

# Reuse fileContent from above:
paragraphs = fileContent.split('\n  ')                  # List of paragraphs from SecondTextFile
numberOfParagraphs = len(paragraphs)

totalNumberOfSentencesInAllParagraphs = 0
for paragraph in paragraphs:
    sentenceInParagraph = paragraph.split('.')          # Split the paragraph in sentences
    numberOfSentencesInParagraph = len(sentenceInParagraph)
    totalNumberOfSentencesInAllParagraphs += numberOfSentencesInParagraph
    if numberOfSentencesInParagraph == 0:                        # This is not a paragraph
        numberOfParagraphs -= 1

averageParagraphLength = totalNumberOfSentencesInAllParagraphs / numberOfParagraphs
print('The average paragraph length is: ' + str(int(averageParagraphLength)) + ' sentences.')
