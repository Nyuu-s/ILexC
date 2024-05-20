import enum
from queue import LifoQueue
import ply.lex as lex

in_path = r"E:\Projects\python\ILexC\in\test.c"



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
    TOKEN_DO = "do operator"
    TOKEN_ASSIGN ="Assign operator"
    TOKEN_IBM_READ_KEY = "IBM read key"
    TOKEN_IBM_READ_FIRST = "IBM read first" 
    TOKEN_IBM_READ_NEXT = "IBM read next"
    TOKEN_IBM_READ_PRIOR = "IBM read prior"
    TOKEN_IBM_R_WRITE = "IBM insert"
    TOKEN_IBM_R_DELETE = "IBM delete"
    TOKEN_IBM_R_UPDATE = "IBM update"
    TOKEN_DOT = "dot operator"
    TOKEN_ARROW = "Arrow operator"
    TOKEN_COMMENT = "Comment"
    TOKEN_MINUS = "Minus"
    TOKEN_PLUS = "Plus"
    TOKEN_NUMBER = "Number"
    TOKEN_STRING = "String"

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
    ".": Token_kind.TOKEN_DOT,
    "=": Token_kind.TOKEN_ASSIGN,
    "-": Token_kind.TOKEN_MINUS
}

COMPOSED_OPERATORS = {
    "<=": Token_kind.TOKEN_LE,
    ">=": Token_kind.TOKEN_GE,
    "==": Token_kind.TOKEN_EQ,
    "->": Token_kind.TOKEN_ARROW,

}

KEYWORDS_TOKEN = {
    "for": Token_kind.TOKEN_FOR,
    "if": Token_kind.TOKEN_IF,
    "while": Token_kind.TOKEN_WHILE,
    "do": Token_kind.TOKEN_DO 
}



IBM_KEYWORDS = {

    "_Rreadk": Token_kind.TOKEN_IBM_READ_KEY,
    "_Rreadn": Token_kind.TOKEN_IBM_READ_NEXT,
    "_Rreadf": Token_kind.TOKEN_IBM_READ_FIRST,
    "_Rreadp": Token_kind.TOKEN_IBM_READ_PRIOR,
    "_Rwrite": Token_kind.TOKEN_IBM_R_WRITE,
    "_Rdelete": Token_kind.TOKEN_IBM_R_DELETE,
    "_Rupdate": Token_kind.TOKEN_IBM_R_UPDATE
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

def is_symbol(x:str):
    return x.isalnum() or x == '_'

def is_literal(x:str):
    return LITERAL_TOKEN.get(x, False) != False

def is_string_start_or_end(x:str):
    return x == '"'

def is_number_start(x:str):
    return x.isnumeric()

def is_number(x:str):
    return x.isalnum() or x == '.'

def eat_line(token: Token, cursor, in_content) -> tuple[Token, int]:
    while cursor < len(in_content) and in_content[cursor] != '\n':
        token.text += in_content[cursor]
        cursor += 1
    return (token, cursor)

def tokenize(in_content: str, cursor: int):

    if cursor >= len(in_content):
        return (Token(Token_kind.TOKEN_END), cursor) 

########## Operators 
    if is_literal(in_content[cursor]):
        token = Token(LITERAL_TOKEN[in_content[cursor]], in_content[cursor])
        cursor += 1
        while (cursor < len(in_content)-1) and is_literal(in_content[cursor]):
            token.text += in_content[cursor]
            cursor += 1
        if (kind := COMPOSED_OPERATORS.get(token.text)) != None:
            token.kind = kind
        
        return (token, cursor)

########## Strings
    if is_string_start_or_end(in_content[cursor]):
        token = Token(Token_kind.TOKEN_STRING, in_content[cursor])
        cursor += 1
    
        while cursor < len(in_content)-1 and in_content[cursor] != "\n" and (not is_string_start_or_end(in_content[cursor]) or in_content[cursor-1] == "\\"):
            token.text += in_content[cursor]
            cursor += 1
        token.text += in_content[cursor]
        cursor += 1
        if token.text.endswith('\n'):
            # multiline single string
            token.kind = Token_kind.TOKEN_UNSUPPORTED
            cursor += 1
            return (token, cursor)
        return (token, cursor)

########## Numbers
    if is_number_start(in_content[cursor]):
        token = Token(Token_kind.TOKEN_NUMBER, in_content[cursor])
        cursor += 1
        while(cursor < len(in_content)-1 and is_number(in_content[cursor])):
            token.text += in_content[cursor]
            cursor += 1
        return (token, cursor)


########## Comments
    if cursor + 2 < len(in_content) and in_content[cursor] == "/" and in_content[cursor+1] == "/":
        token = Token(Token_kind.TOKEN_COMMENT, "")
        return eat_line(token, cursor, in_content)
       

########## Preprocessor
    if in_content[cursor] == "#":
        token = Token(Token_kind.TOKEN_PREPROC, "")
        while True:
            token, cursor = eat_line(token, cursor, in_content)
            if not token.text.endswith("\\"):
                break
            cursor += 1
        return (token, cursor)
    
########## Symbols
    if is_symbol_start(in_content[cursor]):
        token = Token(Token_kind.TOKEN_SYMBOL)
        # get all symbol characters
        while(cursor < len(in_content)-1 and is_symbol(in_content[cursor])):
            token.text += in_content[cursor]
            cursor += 1
        # check if symbol is a reserved keyword 
        if (statement := KEYWORDS_TOKEN.get(token.text, token.kind)) != token.kind:
            token.kind = statement
        return (token, cursor)  

######### Pointers
    # if in_content[cursor] == "*":
    #     if tokens[len(tokens)-1].kind == Token_kind.TOKEN_SYMBOL:
    #         tokens[len(tokens)-1].kind = Token_kind.TOKEN_POINTER
    #     cursor += 1
    #     return (None, cursor)
    
    if in_content[cursor] in IGNORE_LIST:
        cursor += 1
        return (None, cursor)
    
    cursor += 1
    return (Token(Token_kind.TOKEN_UNSUPPORTED, in_content[cursor]), cursor)     


# if not using classes   
tokens: list[Token] = []
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
          
       
# with open(in_path, "r",encoding="utf-8") as f:
#     lexer = Lexer(f.read().strip())
#     while not lexer.is_at_end():
#        lexer.tokenize() 

