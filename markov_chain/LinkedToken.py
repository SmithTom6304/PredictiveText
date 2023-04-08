from simple_text_lexer.Token import Token, TokenType


class LinkedToken(Token):

    def __init__(self, token: Token, next_token):
        super().__init__(token.Type, token.Lexeme, token.Line, token.Position)
        self.NextToken: LinkedToken = next_token
