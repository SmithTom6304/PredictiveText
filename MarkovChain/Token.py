class Token:
    def __init__(self, lexeme):
        self.Lexeme = lexeme
        self.NextNodes = set()

    def __eq__(self, other):
        if other is None:
            return False
        return self.Lexeme == other.Lexeme

    def add_next_node(self, lexeme, existing_tokens):
        existing_node = None
        for node in self.NextNodes:
            if node.Token.Lexeme == lexeme:
                existing_node = node
                break
        if existing_node is not None:
            existing_node.Occurrences += 1
            return existing_node.Token
        else:
            new_token = None
            for token in existing_tokens:
                if token.Lexeme == lexeme:
                    new_token = token
                    break
            if new_token is None:
                new_token = Token(lexeme)
            self.NextNodes.add(TokenConnection(new_token))
            return new_token


class TokenConnection:
    def __init__(self, token):
        self.Token = token
        self.Occurrences = 1
