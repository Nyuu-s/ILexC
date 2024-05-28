from utils.lex.TokenKinds import Token_kind
from enum import Enum

class States(Enum):
    INIT = 0
    DEFAULT = 1
    PREPRO = 2
    SYMBOL_START = 3

    END = 99 

def ToDefaultState():
    return States.DEFAULT

def ToPreproState():
    return States.PREPRO

def ToSymbolStart():
    return States.SYMBOL_START

Transitions = [
    [ToDefaultState], #INIT
    [ToPreproState, ToSymbolStart], #DEFAULT
    [ToDefaultState], #PREPRo
    [ToDefaultState] #SYMBOL_START
]