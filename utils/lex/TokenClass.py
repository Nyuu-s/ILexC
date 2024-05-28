from utils.lex.TokenKinds import Token_kind
from enum import Enum

class TokenCategory(Enum):
    C_FUNC = ['TOKEN_C_']
    IBM_FUNC = ['TOKEN_IBM']
    PREPRO = ['TOKEN_PREPRO']

class Token:

    def is_in_category(self, category: str):
        return TokenCategory.__members__.get(category, False) and TokenCategory[category].value in self.kind.name
    
    def is_in_category(self, category: TokenCategory):
        for cat in category.value:
            if cat in self.kind.name:
                return True
        return False

    def __init__(self, kind, text = "") -> None:
        self.kind: Token_kind = kind
        self.text: str = text