import enum


from utils.lex.TokenKinds import Token_kind
from utils.lex.TokenClass import Token, TokenCategory
from utils.lex.TokenTables import LITERAL_TOKEN, KEYWORDS_TOKEN, COMPOSED_OPERATORS_TOKEN, IBM_FUNCTION_TOKEN, OPERARTORS_TOKEN, C_FUNCTION_TOKEN

in_path = r"in\test.c"


UNSUPPORTED_IGNORE_LIST = [
    " ",
    "\n"
]


def is_symbol_start(x:str):
    return x.isalpha() or x == '_'

def is_symbol(x:str):
    return x.isalnum() or x == '_'

def is_literal(x:str):
    return LITERAL_TOKEN.get(x, False) != False

def is_operator(x:str):
    return OPERARTORS_TOKEN.get(x, False) != False

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

def identify_symbol(symbol: str) -> tuple[Token_kind, TokenCategory]:
   
    if (statement := KEYWORDS_TOKEN.get(symbol, None)) != None:
        return (statement, TokenCategory.KEYWORDS)
     
    if (function := IBM_FUNCTION_TOKEN.get(symbol, None)) != None:
        return (function, TokenCategory.IBM_FUNC)
    
    if (function := C_FUNCTION_TOKEN.get(symbol, None)) != None:
        return (function, TokenCategory.C_FUNC)

    return (Token_kind.TOKEN_SYMBOL, TokenCategory.UNKNOWN)

def tokenize(in_content: str, cursor: int):

    if cursor >= len(in_content):
        return (Token(Token_kind.TOKEN_END), cursor) 

########## Literals
    if is_literal(in_content[cursor]):
        token = Token(LITERAL_TOKEN[in_content[cursor]], in_content[cursor])
        cursor += 1
        return (token, cursor)
    
########## Operators 
    if is_operator(in_content[cursor]):
        token = Token(OPERARTORS_TOKEN[in_content[cursor]], in_content[cursor])
        cursor += 1
        while (cursor < len(in_content)-1) and is_operator(in_content[cursor]):
            token.text += in_content[cursor]
            cursor += 1
        if (kind := COMPOSED_OPERATORS_TOKEN.get(token.text)) != None:
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
        token.category = TokenCategory.PREPRO
        return (token, cursor)
    
########## Symbols
    if is_symbol_start(in_content[cursor]):
        token = Token(Token_kind.TOKEN_SYMBOL)
        # get all symbol characters
        while(cursor < len(in_content)-1 and is_symbol(in_content[cursor])):
            token.text += in_content[cursor]
            cursor += 1

        token.kind, token.category = identify_symbol(token.text)
    
        
        return (token, cursor)  

######### Pointers
    # if in_content[cursor] == "*":
    #     if tokens[len(tokens)-1].kind == Token_kind.TOKEN_SYMBOL:
    #         tokens[len(tokens)-1].kind = Token_kind.TOKEN_POINTER
    #     cursor += 1
    #     return (None, cursor)
    
    if in_content[cursor] in UNSUPPORTED_IGNORE_LIST:
        cursor += 1
        return (None, cursor)
    
    token = Token(Token_kind.TOKEN_UNSUPPORTED, in_content[cursor])
    cursor += 1
    return (token, cursor)


# if not using classes  
def lex():
    tokens: list[Token] = []
    with open(in_path, "r",encoding="utf-8") as f:
        content = f.read().strip()
        _cursor = 0

        while _cursor < len(content):
            cur_token, _cursor = tokenize(content, _cursor)
            if(cur_token != None):
                if cur_token.kind == Token_kind.TOKEN_UNSUPPORTED and tokens[len(tokens)-1].kind == Token_kind.TOKEN_UNSUPPORTED:
                    tokens[len(tokens)-1].text += cur_token.text
                    continue
                tokens.append(cur_token)
        
        for token in tokens:
            if token.kind != Token_kind.TOKEN_UNSUPPORTED:
                print(token.text, f"({token.kind.value})")
    print("###### END LEXING ########")
    return tokens          
    
# with open(in_path, "r",encoding="utf-8") as f:
#     lexer = Lexer(f.read().strip())
#     while not lexer.is_at_end():
#        lexer.tokenize() 

