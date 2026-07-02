# DSL
DSL (Domain Specific Language) is build to solve one specific class of problems exceptionally well and bridge the communication gap between the domain experts (users) and developers.
Consider creating a mini-language tailored to a specific problem domain.

This mini-project is DSL for managing student records.


## PLY (Python Lex-Yacc)
It's a Python library that let's you easily build the core parts of a compiler or interpreter.
### why we used it:
Building a lexer and parser from scratchh is extremely comples and time-consuming. PLY Automates a huge portion of this work.
### how does it work:
provide PLY with the rules of a specific language (regurlar expressions for tokens and context-free grammar for syntax), and PLY handles the rest; generating lexer and parser.


## 1. Lexer :
Reads the sourse code and converts it into tokens.

## 2. Parser :
Checks the token sequence against grammar rules and builds command objects.

## 3. Interpreter: 
Takes the command objects and performs the actual operations on the students dictionary.
