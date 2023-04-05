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