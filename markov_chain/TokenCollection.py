import random

from simple_text_lexer.Token import Token, TokenType
from LinkedToken import LinkedToken


class TokenCollection:

    def __init__(self):
        self.Tokens: list[LinkedToken] = list()

    def add_token(self, token: LinkedToken):
        self.Tokens.append(token)

    def generate_next_token(self) -> Token:
        return random.choice(self.Tokens).NextToken
