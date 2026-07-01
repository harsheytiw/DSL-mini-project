# main.py
# entry point of the project.

import sys
from lexer import Lexer, LexerError
from parser import Parser, ParserError
from interpreter import Interpreter, InterpreterError


def run_file(filename):
    # Read the raw DSL script from the file as plain text.
    try:
        with open(filename, "r") as f:
            source_code = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'.")
        return

    # LEXING - turn raw text into a list of tokens.
    try:
        lexer = Lexer(source_code)
        token_list = lexer.tokenize()
    except LexerError as e:
        print(e)
        return

    # PARSING - turn tokens into a list of structured commands.
    try:
        parser = Parser(token_list)
        command_list = parser.parse()
    except ParserError as e:
        print(e)
        return

    # INTERPRETING - actually execute the commands.
    try:
        interpreter = Interpreter()
        interpreter.run(command_list)
    except InterpreterError as e:
        print(e)
        return

# lets us run the program
if __name__ == "__main__":

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "sample.dsl"

    run_file(filename)
