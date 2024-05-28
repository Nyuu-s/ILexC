from utils.lex.TokenKinds import Token_kind
from utils.lex.TokenClass import TokenCategory
from enum import Enum

class States(Enum):
    DEFAULT = 0
    PREPRO = 1
    SYMBOL_START = 2

    END = 3 

def ToDefaultState():
    print("DEfault ->")
    return States.DEFAULT

def ToPreproState():
    print("Prepro ->")
    return States.PREPRO

def ToSymbolStart():
    return States.SYMBOL_START

def ToEndState():
    print("Reached End")
    return States.END

Transitions = [
    {TokenCategory.PREPRO: ToPreproState, TokenCategory.UNKNOWN: ToEndState}, #DEFAULT
    {TokenCategory.UNKNOWN: ToEndState, TokenCategory.PREPRO: ToPreproState}, #PREPRo
    {} ,#SYMBOL_START
    {} #end
]