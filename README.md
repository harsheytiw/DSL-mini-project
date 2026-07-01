# StudentDSL

A simple **Domain-Specific Language (DSL)** for managing student academic records, built in Python from scratch — including a Lexer, Parser, and Interpreter.

This project was built as a B.Tech mini-project to demonstrate the core concepts of compiler design (lexical analysis, parsing, and interpretation) in a small, beginner-friendly way.

---

## What is StudentDSL?

StudentDSL lets you write plain, readable commands to manage a list of students and their marks — without writing any Python code. For example:

```
ADD STUDENT "Riya" MARKS 85
ADD STUDENT "Aman" MARKS 70
SHOW ALL
AVERAGE
TOPPER
```

Running this script produces:
```
Student Riya added with marks 85.
Student Aman added with marks 70.
Riya -> 85 marks
Aman -> 70 marks
Class Average: 77.5
Topper: Riya with 85 marks
```

---

## Supported Commands

| Command | Description |
|---|---|
| `ADD STUDENT "<name>" MARKS <number>` | Adds a new student with given marks (0–100) |
| `SHOW STUDENT "<name>"` | Displays one student's marks |
| `SHOW ALL` | Displays every student's marks |
| `AVERAGE` | Displays the class average marks |
| `TOPPER` | Displays the student with the highest marks |

Lines starting with `#` are comments and are ignored.

---

## Project Structure

```
StudentDSL/
│
├── tokens.py          # Token type definitions
├── lexer.py            # Converts DSL text into tokens
├── parser.py           # Converts tokens into structured commands
├── interpreter.py      # Executes the structured commands
├── main.py              # Entry point — runs the full pipeline
├── sample.dsl           # Example DSL script
├── tests/                # 10 sample test scripts (valid + invalid)
├── README.md             # This file
└── docs/
    ├── project_report.md
    ├── viva_questions.md
    └── presentation.md
```

---

## How It Works

```
DSL Script (.dsl file)
        |
        v
   [ LEXER ]   ->  breaks text into tokens (ADD, STUDENT, STRING, NUMBER...)
        |
        v
   [ PARSER ]  ->  checks token order against grammar rules, builds command list
        |
        v
 [ INTERPRETER ] -> executes each command, stores data, prints results
        |
        v
     Output
```

---

## Requirements

- Python 3.7 or higher (no external libraries needed — pure standard Python)

## How to Run

```bash
# Clone or download this repository, then:
cd StudentDSL
python3 main.py sample.dsl
```

To run any other script:
```bash
python3 main.py tests/test1_valid_basic.dsl
```

---

## Example: Writing Your Own Script

Create a file `mydata.dsl`:
```
ADD STUDENT "Sara" MARKS 95
ADD STUDENT "Vikram" MARKS 60
SHOW ALL
TOPPER
```

Run it:
```bash
python3 main.py mydata.dsl
```

---

## Error Handling

StudentDSL distinguishes between three types of errors:

1. **Lexer Error** — invalid characters/tokens (e.g. missing quotes around a name)
2. **Parser Error** — tokens in the wrong order (e.g. keywords out of sequence)
3. **Interpreter Error** — logically invalid actions (e.g. negative marks, showing a student that doesn't exist)

---

## Future Scope

- Support for multiple subjects per student
- DELETE / UPDATE commands
- Saving records to a file (persistence)
- Grade calculation (A/B/C based on marks)

---

## Author

Built as a B.Tech 2nd Year Mini Project — Domain-Specific Language Design & Implementation.

## License

This project is free to use for educational purposes.
