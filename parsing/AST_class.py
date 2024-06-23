from utils.lex.TokenClass import Token

from enum import Enum

class NODE_TYPE(Enum):
    PROGRAM = "program",
    PREPROCESSOR_STATEMENT = "PreprocessorStatemen",
    INCLUDE_DIRECTIVE = "IncludeDirective",
    DEFINE_DIRECTIVE = "DefineDirective",
    PRAGMA_DIRECTIVE = "PragmaDirective"
    INCLUDE_FILE = "IncludeFile"

    UNRECOGNIZED = "Not implemented yet"

class Node():
    kind = None
    value = None
    children = []

    pass

class AST():
    root = {
        "type": NODE_TYPE.PROGRAM,
        "children": []
    }

        
    