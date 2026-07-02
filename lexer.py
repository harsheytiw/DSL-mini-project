# lexer.py

import ply.lex as lex
import tokens as tok


class LexerError(Exception):
    pass


class Lexer:
    tokens = tok.TOKENS
    t_ignore = " \t"

    def __init__(self, source_code):
        self.source = source_code
        self.lexer = lex.lex(module=self)

    def t_STRING(self, t):
        r'"([^"\n])*"'
        t.value = t.value[1:-1]
        return t

    def t_NUMBER(self, t):
        r'-?\d+'
        t.value = int(t.value)
        return t

    def t_COMMENT(self, t):
        r'\#.*'
        pass

    def t_WORD(self, t):
        r'[A-Za-z]+'
        token_type = tok.KEYWORDS.get(t.value)
        if token_type is None:
            raise LexerError(
                f"Lexer Error (line {t.lineno}): Unknown word '{t.value}'. "
                "Did you forget quotes around a name?"
            )
        t.type = token_type
        return t

    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    def t_error(self, t):
        raise LexerError(
            f"Lexer Error (line {t.lineno}): Unexpected character '{t.value[0]}'."
        )

    def tokenize(self):
        self.lexer.input(self.source)
        token_list = []

        while True:
            token = self.lexer.token()
            if token is None:
                break
            token_list.append(tok.Token(token.type, token.value, token.lineno, token.lexpos))

        return token_list
