# Longest-Compound-Word
Promblem statement given by Impledge


Problem Statement
Write a program that:
  1. Reads provided files (Input_01.txt and Input_02.txt) containing alphabetically sorted words list (one
  word per line, no spaces, all lower case)
  2. Identifies & display below given data in logs/console/output file
      o longest compounded word
      o second longest compounded word
      o time taken to process the input file
  Note: A compounded word is one that can be constructed by combining (concatenating) shorter words
  also found in the same file

Solution :

Created two function first one is a recursive function which returns a list of compounded word. It defines an inner function called "isConcat" which is used to check if a given word is a concatenated word. It uses memoization (caching) to improve the performance of the function by storing previously computed results. The function takes a word as input and iterates through all possible prefixes and suffixes of that word to determine if it can be formed by concatenating other words in the wordSet. If it finds a valid combination, it returns True; otherwise, it returns False.

Second function simply returns the largest and second largest word from the given by comparing all values
