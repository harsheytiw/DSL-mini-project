# parser.py

import ply.yacc as yacc
import tokens as tok


class ParserError(Exception):
    pass


# Each class below represents ONE TYPE of valid DSL command.
# After parsing, we end up with a list of these objects.
# The Interpreter will later look at each object's type and act accordingly.

class AddStudentCommand:
    def __init__(self, name, marks, line):
        self.name = name
        self.marks = marks
        self.line = line

    def __repr__(self):
        return f"AddStudentCommand(name={self.name}, marks={self.marks})"


class ShowStudentCommand:
    def __init__(self, name, line):
        self.name = name
        self.line = line

    def __repr__(self):
        return f"ShowStudentCommand(name={self.name})"


class ShowAllCommand:
    def __init__(self, line):
        self.line = line

    def __repr__(self):
        return "ShowAllCommand()"


class AverageCommand:
    def __init__(self, line):
        self.line = line

    def __repr__(self):
        return "AverageCommand()"


class TopperCommand:
    def __init__(self, line):
        self.line = line

    def __repr__(self):
        return "TopperCommand()"


class Parser:
    tokens = tok.TOKENS

    class TokenStream:
        def __init__(self, token_list):
            self.tokens = iter(token_list)

        def token(self):
            try:
                token = next(self.tokens)
                return token
            except StopIteration:
                return None

    def __init__(self, token_list):
        self.token_list = token_list
        self.parser = yacc.yacc(module=self, debug=False)

    def parse(self):
        result = self.parser.parse(lexer=self.TokenStream(self.token_list), debug=False)
        return result if result is not None else []

    def p_program(self, p):
        "program : statements"
        p[0] = p[1]

    def p_statements(self, p):
        "statements : statements statement"
        p[0] = p[1] + [p[2]]

    def p_statements_single(self, p):
        "statements : statement"
        p[0] = [p[1]]

    def p_statement_add(self, p):
        "statement : ADD STUDENT STRING MARKS NUMBER"
        p[0] = AddStudentCommand(p[3], p[5], p.lineno(1))

    def p_statement_show_all(self, p):
        "statement : SHOW ALL"
        p[0] = ShowAllCommand(p.lineno(1))

    def p_statement_show_student(self, p):
        "statement : SHOW STUDENT STRING"
        p[0] = ShowStudentCommand(p[3], p.lineno(1))

    def p_statement_average(self, p):
        "statement : AVERAGE"
        p[0] = AverageCommand(p.lineno(1))

    def p_statement_topper(self, p):
        "statement : TOPPER"
        p[0] = TopperCommand(p.lineno(1))

    def p_error(self, p):
        if p is None:
            raise ParserError("Parser Error: Unexpected end of input.")
        raise ParserError(
            f"Parser Error (line {p.lineno}): Unexpected token '{p.type}'."
        )
