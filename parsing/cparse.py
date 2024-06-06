

from enum import Enum
import os
print(os.getcwd())

from utils.lex.TokenClass import Token, TokenCategory
from utils.lex.TokenKinds import Token_kind
from utils.lex.clex import lex
from utils.parse.TransitionTable import Transitions, States
from parsing.AST_class import AST, NODE_TYPE

def process_symbol(token: Token):
    #detect function definitions or uses 
    pass
class CParse():



    
    def __init__(self) -> None:
        self.functions_definitions = []
        self.current_token_pile = []
        self.current_state = States.DEFAULT

    def parse_tokens(self, tokens: list):
        tree = AST()
        current_token = tokens.pop(0)
        for i in range(len(tokens)-1):
            match current_token.kind:
                case Token_kind.TOKEN_PREPROC:  
                    tree.root["children"].append(tree.PreprocessorStatement(current_token))
                case Token_kind.TOKEN_SYMBOL:
                    pass
            current_token = tokens.pop(i)
        print(tree.root)
        


parser = CParse()
parser.parse_tokens(lex())
