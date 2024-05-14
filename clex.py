import enum
from queue import LifoQueue
import ply.lex as lex

in_path = r"E:\Projects\python\CParser\in\test.c"



class Token_kind(enum.Enum):
    TOKEN_END = "end"
    TOKEN_PREPROC = "preprocessor directive"
    TOKEN_SYMBOL = "Symbol"
    TOKEN_POINTER = "raw pointer"
    TOKEN_OPEN_PAR = "open parenthesis"
    TOKEN_CLOSE_PAR = "close parenthesis"
    TOKEN_OPEN_CURLY = "open curly brace"
    TOKEN_CLOSE_CURLY = "close curly brace"
    TOKEN_SEMICOLON = "semicolon"
    TOKEN_FOR = "for loop"
    TOKEN_WHILE = "while loop"
    TOKEN_IF = "if statement"
    TOKEN_GT = "Greater than"
    TOKEN_LT = "Less than"
    TOKEN_GE = "Greater or equal"
    TOKEN_LE = "Less or equal"
    TOKEN_EQ = "Equal"
    TOKEN_NOT = "Not operator"
    TOKEN_IBM_READ_KEY = "IBM read key"
    TOKEN_COMMENT = "Comment"
    

    TOKEN_UNSUPPORTED = "invalid token"

LITERAL_TOKEN = {
    "(": Token_kind.TOKEN_OPEN_PAR,
    ")": Token_kind.TOKEN_CLOSE_PAR,
    "{": Token_kind.TOKEN_OPEN_CURLY,
    "}": Token_kind.TOKEN_CLOSE_CURLY,
    ";": Token_kind.TOKEN_SEMICOLON,
    "!": Token_kind.TOKEN_NOT,
    "<": Token_kind.TOKEN_LT,
    ">": Token_kind.TOKEN_GT,
    "<=": Token_kind.TOKEN_LE,
    ">=": Token_kind.TOKEN_GE,
}

STATEMENTS_TOKEN = {
    "for": Token_kind.TOKEN_FOR,
    "if": Token_kind.TOKEN_IF,
    "while": Token_kind.TOKEN_WHILE, 
    "_Rreadk": Token_kind.TOKEN_IBM_READ_KEY
}
IGNORE_LIST = [
    " "
]
context_stack = LifoQueue(100)


class Token:
    def __init__(self, kind, text = "") -> None:
        self.kind = kind
        self.text = text

def is_symbol_start(x:str):
    return x.isalpha() or x == '_'

def is_special_symbol(x:str): 
    return x == '(' or x == ')' or x == '{' or x == '}' or x == '[' or x == ']' 

def is_symbol(x:str):
    return x.isalnum() or x == '_'

tokens: list[Token] = []    
def tokenize(in_content: str, cursor: int):

    if cursor >= len(in_content):
        return (Token(Token_kind.TOKEN_END), cursor)

    
   
    if (token_kind := LITERAL_TOKEN.get(in_content[cursor], None)) != None:
        token = Token(token_kind, in_content[cursor])
        cursor += 1
        return (token, cursor)

    if cursor + 2 < len(in_content) and in_content[cursor] == "/" and in_content[cursor+1] == "/":
        token = Token(Token_kind.TOKEN_COMMENT, "")
        #TODO: Refacto in func
        while cursor < len(in_content) and in_content[cursor] != '\n':
            token.text += in_content[cursor]
            cursor += 1
        return (token, cursor)

    if in_content[cursor] == "#":
        token = Token(Token_kind.TOKEN_PREPROC, in_content[cursor])
        #TODO: Refacto in func
        while cursor < len(in_content) and in_content[cursor] != '\n':
            token.text += in_content[cursor]
            cursor += 1
        return (token, cursor)
    

    if is_symbol_start(in_content[cursor]):
        token = Token(Token_kind.TOKEN_SYMBOL)
        # get all symbol characters
        while(cursor < len(in_content) and is_symbol(in_content[cursor])):
            token.text += in_content[cursor]
            cursor += 1
        # check if symbol is a reserved statement 
        if (statement := STATEMENTS_TOKEN.get(token.text, token.kind)) != token.kind:
            token.kind = statement
        return (token, cursor)  

    if in_content[cursor] == "*":
        if tokens[len(tokens)-1].kind == Token_kind.TOKEN_SYMBOL:
            tokens[len(tokens)-1].kind = Token_kind.TOKEN_POINTER
        cursor += 1
        return (None, cursor)
    
    if in_content[cursor] in IGNORE_LIST:
        cursor += 1
        return (None, cursor)
    
    cursor += 1
    return (Token(Token_kind.TOKEN_UNSUPPORTED, ""), cursor)     



with open(in_path, "r",encoding="utf-8") as f:
    content = f.read().strip()
    _cursor = 0
    while _cursor < len(content):
        cur_token, _cursor = tokenize(content, _cursor)
        if(cur_token != None):
            tokens.append(cur_token)
    
    for token in tokens:
        if token.kind != Token_kind.TOKEN_UNSUPPORTED:
            print(token.text, f"({token.kind.value})")
          
       

