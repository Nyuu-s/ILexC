from utils.lex.TokenClass import Token

from enum import Enum

class NODE_TYPE(Enum):
    PROGRAM = "program",
    PREPROCESSOR_STATEMENT = "PreprocessorStatemen",
    INCLUDE_DIRECTIVE = "IncludeDirective",
    DEFINE_DIRECTIVE = "DefineDirective",
    PRAGMA_DIRECTIVE = "PragmaDirective"
    INCLUDE_FILE = "IncludeFile"



class Node():
    kind = None
    value = None
    children = []

    pass

class AST():
    root = {
        "type": NODE_TYPE[0],
        "children": []
    }
    def __helper_create_node(self, type, text):
        return {
            "type": type,
            "value": text,
            "children" : []
        }
    def IncludeDirective(self, token: Token):
        split = token.text.split('#include')
        node = self.__helper_create_node(NODE_TYPE.INCLUDE_DIRECTIVE, split[0] )
        node["children"].append(self.__helper_create_node(NODE_TYPE.INCLUDE_FILE, split[1] ))
        return node

    def DefineDirective(self, token: Token):
        split = token.text.split('#define')
        node = self.__helper_create_node(NODE_TYPE.DEFINE_DIRECTIVE, split[0] )

        #TODO: handle child
        return node
      
    def PragmaDirective(self, token: Token):
        split = token.text.split('#pragma')
        node = self.__helper_create_node(NODE_TYPE.PRAGMA_DIRECTIVE, split[0] )
        #TODO: handle child
        return node
    def PreprocessorStatement(self, token: Token):
        node = self.__helper_create_node(NODE_TYPE.PREPROCESSOR_STATEMENT, token.text)

        if token.text.startswith('#include'):
            node["children"].append(self.IncludeDirective(token))
        elif token.text.startswith('#define'): 
            node["children"].append(self.DefineDirective(token))
        elif token.text.startswith("#pragma"):
            node["children"].append(self.PragmaDirective)
        
        return node
        
    