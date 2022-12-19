# CreateModel.py
import sys

class Token:
    def __init__(self, lexeme):
        self.lexeme = lexeme
        self.nextNodes = set()
    def __eq__(self, other):
        if(other == None):
            return False
        return self.lexeme == other.lexeme
    def AddNextNode(self, lexeme, existingTokens):
        existingNode = None
        for node in self.nextNodes:
            if node.token.lexeme == lexeme:
                existingNode = node
                break
        if existingNode != None:
            existingNode.occurences += 1
            return existingNode.token
        else:
            tokenExists = False
            newToken = None
            for token in existingTokens:
                if token.lexeme == lexeme:
                    newToken = token
                    break
            if newToken == None:
                newToken = Token(lexeme)
            self.nextNodes.add(TokenConnection(newToken))
            return newToken


class TokenConnection:
    def __init__(self, token):
        self.token = token
        self.occurences = 1

if __name__ == "__main__":
    testSentence = "Scolding is something common in student life. Being a naughty boy, I am always scolded by my parents. But one day I was severely scolded by my English teacher. She infect teaches well. But that day, I could not resist the temptation that an adventure of Nancy Drew offered. While she was teaching, I was completely engrossed in reading that book. Nancy Drew was caught in the trap laid by some smugglers and it was then when I felt a light tap on my bent head. The teacher had caught me red handed. She scolded me then and there and insulted me in front of the whole class. I was embarrassed. My cheeks burned being guilty conscious. When the class was over, I went to the teacher to apologize. When she saw that I had realized my mistake, she cooled down and then told me in a very kind manner how disheartening it was when she found any student not paying attention. I was genuinely sorry and promised to myself never to commit such a mistake again."
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
        prevToken = prevToken.AddNextNode(word, tokens)
        if not prevToken in tokens:
            tokens.append(prevToken)
    for token in tokens:
        print(token.lexeme + ":")
        for connection in token.nextNodes:
            print("\t" + connection.token.lexeme + ": " + str(connection.occurences))





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


