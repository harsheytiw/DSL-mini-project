# parser.py


import tokens as tok


class ParserError(Exception):
    """A custom error type just for parser problems (like wrong word order)."""
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
    def __init__(self, token_list):
        self.tokens = token_list
        self.pos = 0  # index of the CURRENT token we are looking at

    def current_token(self):
        """Returns the token we are currently looking at."""
        return self.tokens[self.pos]

    def advance(self):
        """Moves forward to the next token."""
        self.pos += 1

    def expect(self, expected_type):
        token = self.current_token()
        if token.type == expected_type:
            self.advance()
            return token
        else:
            raise ParserError(
                f"Parser Error (line {token.line}): Expected '{expected_type}' "
                f"but found '{token.type}' ({repr(token.value)})."
            )

    def parse(self):
        commands = []
        while self.current_token().type != tok.EOF:
            command = self.parse_statement()
            commands.append(command)
        return commands

    def parse_statement(self):
        token = self.current_token()

        if token.type == tok.ADD:
            return self.parse_add_statement()
        elif token.type == tok.SHOW:
            return self.parse_show_statement()
        elif token.type == tok.AVERAGE:
            line = token.line
            self.advance()
            return AverageCommand(line)
        elif token.type == tok.TOPPER:
            line = token.line
            self.advance()
            return TopperCommand(line)
        else:
            raise ParserError(
                f"Parser Error (line {token.line}): Unexpected token "
                f"'{token.type}'. Expected a command (ADD, SHOW, AVERAGE, TOPPER)."
            )

    def parse_add_statement(self):
        line = self.current_token().line
        self.expect(tok.ADD)
        self.expect(tok.STUDENT)
        name_token = self.expect(tok.STRING)
        self.expect(tok.MARKS)
        marks_token = self.expect(tok.NUMBER)

        return AddStudentCommand(name_token.value, marks_token.value, line)

    def parse_show_statement(self):
        line = self.current_token().line
        self.expect(tok.SHOW)

        if self.current_token().type == tok.ALL:
            self.advance()
            return ShowAllCommand(line)
        elif self.current_token().type == tok.STUDENT:
            self.advance()
            name_token = self.expect(tok.STRING)
            return ShowStudentCommand(name_token.value, line)
        else:
            token = self.current_token()
            raise ParserError(
                f"Parser Error (line {token.line}): Expected 'ALL' or 'STUDENT' "
                f"after SHOW, but found '{token.type}'."
            )
