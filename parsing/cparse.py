

from enum import Enum
import os
print(os.getcwd())

from utils.lex.TokenClass import Token, TokenCategory
from utils.lex.TokenKinds import Token_kind
from utils.lex.clex import lex
from utils.parse.TransitionTable import Transitions, States
from AST_class import AST, NODE_TYPE

def process_symbol(token: Token):
    #detect function definitions or uses 
    pass
class CParse():
    def __init__(self) -> None:
        self.functions_definitions = []
        self.token_pile = []
        self.current_state = States.DEFAULT

    def parse_tokens(self, tokens: list):
        print("##### START BUILDING AST #####")
        tree = AST()
        i = 0
        current_token = tokens.pop(i)  
        while len(tokens) > 0:
            if current_token.category == TokenCategory.PREPRO:
                    print("cat: ", current_token.category)
                    tree.root["children"].append(tree.PreprocessorStatement(current_token))
            elif current_token.category == TokenCategory.KEYWORDS:
                    
                    pass
    
            current_token = tokens.pop(i)
        print(tree.root)
        


parser = CParse()
parser.parse_tokens(lex())
