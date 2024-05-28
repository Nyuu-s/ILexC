

from enum import Enum
from utils.lex.TokenClass import Token, TokenCategory
from utils.lex.TokenKinds import Token_kind
from clex import lex
from utils.parse.TransitionTable import Transitions, States


def process_symbol(token: Token):
    #detect function definitions or uses 
    pass
class CParse():



    
    def __init__(self) -> None:
        self.functions_definitions = []
        self.current_token_pile = []
        self.current_state = States.DEFAULT

    def parse_tokens(self, tokens):
        token_count = 0
        current_token: Token = tokens[token_count]
        while token_count < len(tokens)-1 and current_token.kind != Token_kind.TOKEN_END:
            # print(current_token.category)
            f = Transitions[self.current_state.value].get(current_token.category, None)
            if f != None:
                self.current_state = f()


            token_count += 1
            current_token = tokens[token_count]
            pass

parser = CParse()
parser.parse_tokens(lex())
