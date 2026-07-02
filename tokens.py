# tokens.py

ADD = "ADD"
STUDENT = "STUDENT"
MARKS = "MARKS"
SHOW = "SHOW"
ALL = "ALL"
AVERAGE = "AVERAGE"
TOPPER = "TOPPER"

STRING = "STRING"
NUMBER = "NUMBER"
EOF = "EOF"  # End Of File

KEYWORDS = {
    "ADD": ADD,
    "STUDENT": STUDENT,
    "MARKS": MARKS,
    "SHOW": SHOW,
    "ALL": ALL,
    "AVERAGE": AVERAGE,
    "TOPPER": TOPPER,
}

TOKENS = [
    ADD,
    STUDENT,
    MARKS,
    SHOW,
    ALL,
    AVERAGE,
    TOPPER,
    STRING,
    NUMBER,
]


class Token:
    def __init__(self, type_, value, line, lexpos=0):
        self.type = type_
        self.value = value
        self.line = line
        self.lexpos = lexpos

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)}, line={self.line})"
