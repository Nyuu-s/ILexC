class Lexer:

    def __init__(self, in_content) -> None:
        self.tokens: list[Token] = []        
        self.content = in_content
        self.cursor = 0
        self.current_token = Token(Token_kind.TOKEN_UNSUPPORTED)
    
    def is_at_end(self):
        return self.cursor >= len(self.content)
    
    def tokenize(self) -> Token:
        if self.cursor >= len(self.content):
            self.current_token.kind = Token_kind.TOKEN_END
            return self.current_token

    def eat_chars( self, number: int):
        for _ in range(number):
            self.current_token.text += self.content[self.cursor]
            self.cursor += 1 
    
    def eat_line(self):
        while self.cursor < len(self.content) and self.content[self.cursor] != '\n':
            self.current_token.text += self.content[self.cursor]

