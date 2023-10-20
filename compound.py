def findAllConcatenatedWordsInADict(words):

        wordSet = set(words)
        ans=[]
        # recursive function to check if a word is concatenated
        @functools.lru_cache(None)  # Memoize the function with least-recently-used cache
        def isConcat(word: str) -> bool:
            for i in range(1, len(word)):  
                prefix = word[:i]  # Get the prefix of the split
                suffix = word[i:]  # Get the suffix of the split
                if prefix in wordSet and (suffix in wordSet or isConcat(suffix)):
                    # concatenated
                    return True
            return False

        # Use a list to get all concatenated words

        for i in words:
            if(isConcat(i)):
                ans.append(i)

        return ans



#function to find longest and second longest compound word
def two_largest_word(words):
    if not words:
        return None, None  # Handle the case of an empty list

    longest_word = ""
    second_longest_word = ""

    for w in words:
        if len(w) > len(longest_word):
            second_longest_word = longest_word
            longest_word = w
        elif len(w) > len(second_longest_word) and w != longest_word:
            second_longest_word = w

    return longest_word, second_longest_word

            ########################################
            ########### START HERE #################
            ########################################

import time
import functools

#Start time counter
start_time = time.time()

# list to store the words extracted from txt file
words = []
con_words = []
# opening the txt file as f 
with open("Input_02.txt", 'r') as f:
    
    for line in f:
        w = line.strip()  # removing leading and trailing whitespace
        if w:  
            words.append(w)

con_words = findAllConcatenatedWordsInADict(words)
#print(con_words)

a,b = two_largest_word(con_words)
print("Longest Compound Word : ", a)
print("Second Longest Compound Word : ", b)

#Stop time counter
end_time = time.time()

# Calculate the execution time in milliseconds
execution_time_ms = (end_time - start_time) * 1000

print("Execution time: {:.5f} milli seconds".format(execution_time_ms))