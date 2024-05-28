

from enum import Enum
from utils.lex.TokenClass import Token, TokenCategory
from utils.lex.TokenKinds import Token_kind
from clex import lex


def process_symbol(token: Token):
    #detect function definitions or uses 
    pass
class CParse():


    def __compute_token_categories(self):
        pass

  
    
    def __init__(self) -> None:
        self.functions_definitions = []
        self.current_token_pile = []
       

    def parse_tokens(self, tokens):
        token_count = 0
        current_token: Token = tokens[token_count]
        while token_count < len(tokens)-1 and current_token.kind != Token_kind.TOKEN_END:

            if current_token.is_in_category(TokenCategory.PREPRO):
                print(current_token.text)
            token_count += 1
            current_token = tokens[token_count]
            pass

parser = CParse()
parser.parse_tokens(lex())
