

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
<<<<<<< HEAD
                    print("cat: ", current_token.category)
                    tree.root["children"].append(self.PreprocessorStatement(current_token))
=======
                    tree.root["children"].append(tree.PreprocessorStatement(current_token))
>>>>>>> 297a56f60275aca8d248d61b4fe78a2f5cb7bc2a
            elif current_token.category == TokenCategory.KEYWORDS:
                self.token_pile.append(current_token)
                tree.root["children"].append(tree.KeyWordIdentifying(current_token))
                current_token = tokens.pop(i)     
            
    
            current_token = tokens.pop(i)
        print(tree.root)

    def __helper_create_node(self, type, text):
        return {
            "type": type,
            "value": text,
            "children" : []
        }
    
    def IncludeDirective(self, token: Token):
        include = "#include"
        split = token.text.split(include)
        node = self.__helper_create_node(NODE_TYPE.INCLUDE_DIRECTIVE, include )
        node["children"].append(self.__helper_create_node(NODE_TYPE.INCLUDE_FILE, split[1] ))
        return node

    def DefineDirective(self, token: Token):
        split = token.text.split('#define')
        node = self.__helper_create_node(NODE_TYPE.DEFINE_DIRECTIVE, split[0] )

        #TODO: handle child
        return node
      
    def PragmaDirective(self, token: Token):
        pragma = "#pragma"
        split = token.text.split(pragma)
        print(split, token.text)
        node = self.__helper_create_node(NODE_TYPE.PRAGMA_DIRECTIVE, pragma )
        match split[1].strip().strip(';'):
            case 'once': 
                node = self.__helper_create_node(NODE_TYPE.PRAGMA_DIRECTIVE, 'once')
            case _:
                node["children"].append(self.__helper_create_node(NODE_TYPE.UNRECOGNIZED, token.text))
            
        return node
    def PreprocessorStatement(self, token: Token):
        node = self.__helper_create_node(NODE_TYPE.PREPROCESSOR_STATEMENT, token.text)

        if token.text.startswith('#include'):
            node["children"].append(self.IncludeDirective(token))
        elif token.text.startswith('#define'): 
            node["children"].append(self.DefineDirective(token))
        elif token.text.startswith("#pragma"):
            node["children"].append(self.PragmaDirective(token))
        else:
             node["children"].append(self.__helper_create_node(NODE_TYPE.UNRECOGNIZED, token.text))
        return node


parser = CParse()
parser.parse_tokens(lex())
