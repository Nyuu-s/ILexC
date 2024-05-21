from enum import Enum

class Token_kind(Enum):
    ### RAW C ###
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
    TOKEN_DOT = "dot operator"
    TOKEN_ARROW = "Arrow operator"
    TOKEN_COMMENT = "Comment"
    TOKEN_MINUS = "Minus"
    TOKEN_PLUS = "Plus"
    TOKEN_NUMBER = "Number"
    TOKEN_STRING = "String"


    ### IBM RELATED ###
    TOKEN_IBM_READ_KEY = "IBM read key"
    TOKEN_IBM_READ_FIRST = "IBM read first" 
    TOKEN_IBM_READ_NEXT = "IBM read next"
    TOKEN_IBM_READ_PRIOR = "IBM read prior"
    TOKEN_IBM_R_WRITE = "IBM insert"
    TOKEN_IBM_R_DELETE = "IBM delete"
    TOKEN_IBM_R_UPDATE = "IBM update"
    TOKEN_IBM_QUSCRTUS = "IBM Create user space"





    TOKEN_UNSUPPORTED = "invalid token"