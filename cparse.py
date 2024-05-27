


from utils.lex.TokenClass import Token
from utils.lex.TokenKinds import Token_kind

def process_symbol(token: Token):
    #detect function definitions or uses 
    pass

class CParse():
    def __init__(self) -> None:
        self.functions_definitions = []
        self.current_token_pile = []

    def parse_tokens(self, tokens):
        token_count = 0
        current_token = tokens[token_count]
        while current_token.kind != Token_kind.TOKEN_END:
            self.current_token_pile.append(current_token)
            
            match tokens[token_count].kind:
                case Token_kind.TOKEN_SYMBOL:
                    process_symbol(current_token)
            
            if token_count > len(tokens):
                break
            token_count += 1