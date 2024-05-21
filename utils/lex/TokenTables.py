from TokenKinds import Token_kind

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

COMPOSED_OPERATORS_TOKEN = {
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



IBM_KEYWORDS_TOKEN = {

    "_Rreadk": Token_kind.TOKEN_IBM_READ_KEY,
    "_Rreadn": Token_kind.TOKEN_IBM_READ_NEXT,
    "_Rreadf": Token_kind.TOKEN_IBM_READ_FIRST,
    "_Rreadp": Token_kind.TOKEN_IBM_READ_PRIOR,
    "_Rwrite": Token_kind.TOKEN_IBM_R_WRITE,
    "_Rdelete": Token_kind.TOKEN_IBM_R_DELETE,
    "_Rupdate": Token_kind.TOKEN_IBM_R_UPDATE
}