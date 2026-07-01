# lexer.py

import tokens as tok


class LexerError(Exception):
    pass


class Lexer:
    def __init__(self, source_code):
        self.source = source_code      
        self.pos = 0                   
        self.line = 1                 

    def current_char(self):
        if self.pos >= len(self.source):
            return None
        return self.source[self.pos]

    def advance(self):
        if self.current_char() == "\n":
            self.line += 1
        self.pos += 1

    def peek(self):
        peek_pos = self.pos + 1
        if peek_pos >= len(self.source):
            return None
        return self.source[peek_pos]

    def skip_whitespace(self):
        while self.current_char() is not None and self.current_char() in " \t\n\r":
            self.advance()

    def skip_comment(self):
        while self.current_char() is not None and self.current_char() != "\n":
            self.advance()

    def read_string(self):
        start_line = self.line
        self.advance()  
        result = ""
        while self.current_char() is not None and self.current_char() != '"':
            result += self.current_char()
            self.advance()

        if self.current_char() is None:
            
            raise LexerError(
                f"Lexer Error (line {start_line}): Missing closing quote (\") for string."
            )

        self.advance()  
        return tok.Token(tok.STRING, result, start_line)

    def read_number(self):
        start_line = self.line
        result = ""
        while self.current_char() is not None and self.current_char().isdigit():
            result += self.current_char()
            self.advance()
        return tok.Token(tok.NUMBER, int(result), start_line)

    def read_word(self):
        start_line = self.line
        result = ""
        while self.current_char() is not None and self.current_char().isalpha():
            result += self.current_char()
            self.advance()

        if result in tok.KEYWORDS:
            return tok.Token(tok.KEYWORDS[result], result, start_line)
        else:
            raise LexerError(
                f"Lexer Error (line {start_line}): Unknown word '{result}'. "
                f"Did you forget quotes around a name?"
            )

    def tokenize(self):
        token_list = []

        while self.current_char() is not None:
            ch = self.current_char()

            if ch in " \t\n\r":
                self.skip_whitespace()
                continue

            if ch == "#":
                self.skip_comment()
                continue

            if ch == '"':
                token_list.append(self.read_string())
                continue

            if ch.isdigit():
                token_list.append(self.read_number())
                continue

            if ch == "-" and self.peek() is not None and self.peek().isdigit():
                start_line = self.line
                self.advance()  
                num_token = self.read_number()
                token_list.append(tok.Token(tok.NUMBER, -num_token.value, start_line))
                continue

            if ch.isalpha():
                token_list.append(self.read_word())
                continue

            raise LexerError(
                f"Lexer Error (line {self.line}): Unexpected character '{ch}'."
            )

        token_list.append(tok.Token(tok.EOF, None, self.line))
        return token_list
