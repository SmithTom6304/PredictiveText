# CreateModel.py
import sys
from Token import Token

if __name__ == "__main__":
    with open('Frankenstein.txt') as f:
        lines = f.readlines()
    testSentence = lines[0]
    tokens = list()
    prePunctuation = ["("]
    postPunctuation = [" ", ",", ".", "!", "?", ":", ";", ")"]
    for punc in prePunctuation:
        testSentence = testSentence.replace(punc, punc + " ")
    for punc in postPunctuation:
        testSentence = testSentence.replace(punc, " " + punc)

    words = testSentence.split()
    prevToken = Token(words[0])
    tokens.append(prevToken)
    print(words[1:])
    for word in words[1:]:
        prevToken = prevToken.add_next_node(word, tokens)
        if not prevToken in tokens:
            tokens.append(prevToken)
    for token in tokens:
        print(token.Lexeme + ":")
        for connection in token.NextNodes:
            print("\t" + connection.Token.Lexeme + ": " + str(connection.Occurrences))





def CreateModel(path):
    print("Create model")

# Parse step:
# Read file
# Delimit on space
# Foreach value
# Check if word contains punctuation
    # If it does, split it
# Add to list

# Model step
# Foreach word in list


