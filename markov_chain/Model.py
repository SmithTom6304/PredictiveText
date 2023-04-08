from Token import Token, TokenType
from LinkedToken import LinkedToken
from TokenCollection import TokenCollection


class Model:
    def __init__(self):
        self.Tokens: dict[str, TokenCollection] = dict()

    def generate_model(self, tokens: list[Token]):
        prev_token: LinkedToken | None = None
        for token in tokens:
            if token.Type in [TokenType.SPACE, TokenType.NEWLINE]:
                continue

            linked_token = LinkedToken(token, None)

            if prev_token is not None:
                prev_token.NextToken = linked_token

            if linked_token.Lexeme not in self.Tokens:
                self.Tokens[linked_token.Lexeme] = TokenCollection()
            self.Tokens[linked_token.Lexeme].add_token(linked_token)

            prev_token = linked_token

    def generate_text(self, max_words: int = 50) -> str:
        prev_word = "."
        generated_text = ""
        words = 0
        while words < max_words:
            next_token = self.Tokens[prev_word].generate_next_token()
            prev_word = next_token.Lexeme
            if next_token.Type is TokenType.WORD:
                generated_text = generated_text + " "
            generated_text = generated_text + prev_word
            words += 1
        return generated_text
