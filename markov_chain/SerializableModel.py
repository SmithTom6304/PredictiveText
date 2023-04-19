import random

from Token import Token, TokenType
from TokenCollection import TokenCollection


class SerializableToken:
    Lexeme: str
    Type: TokenType

    def __init__(self, lexeme: str, token_type: TokenType):
        self.Lexeme = lexeme
        self.Type = token_type
        random.seed()

    def __eq__(self, obj):
        return isinstance(obj, SerializableToken) and self.Lexeme == obj.Lexeme

    def __key(self) -> tuple[str, TokenType]:
        return (self.Lexeme, self.Type)

    def __hash__(self):
        return hash(self.__key())


class SerializableModel:
    def __init__(self):
        self.Tokens: dict[str, dict[SerializableToken, int]] = dict()

    def generate_model(self, tokens: list[Token]):
        prev_token: str | None = None
        for token in tokens:

            if token.Type in [TokenType.SPACE, TokenType.NEWLINE]:
                continue

            serializable_token = SerializableToken(token.Lexeme, token.Type)

            if prev_token is not None:
                if prev_token not in self.Tokens:
                    self.Tokens[prev_token] = dict()
                token_occurrences = self.Tokens[prev_token]
                if serializable_token not in token_occurrences:
                    token_occurrences[serializable_token] = 0
                token_occurrences[serializable_token] = token_occurrences.get(serializable_token) + 1

            prev_token = serializable_token.Lexeme

    def generate_text(self, max_words: int = 50) -> str:
        prev_word = "."
        generated_text = ""
        words = 0
        while words < max_words:
            # next_token = self.Tokens[prev_word].generate_next_token()
            next_token = self.generate_next_token(prev_word)
            prev_word = next_token.Lexeme
            if next_token.Type is TokenType.WORD:
                generated_text = generated_text + " "
            generated_text = generated_text + prev_word
            words += 1
        return generated_text

    def generate_next_token(self, word: str) -> SerializableToken | None:
        if word not in self.Tokens:
            return None
        candidates: dict[SerializableToken, int] = self.Tokens.get(word)

        index: int = 0
        candidate_chance: list[tuple[SerializableToken, int]] = list()
        for candidate in candidates.items():
            candidate_chance.append((candidate[0], candidate[1] + index))
            index += candidate[1]

        choice = random.randrange(index)

        result = candidate_chance[0][0]
        for candidate in candidate_chance:
            if candidate[1] > choice:
                return result
            result = candidate[0]


