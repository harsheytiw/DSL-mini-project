# interpreter.py

from parser import (
    AddStudentCommand,
    ShowStudentCommand,
    ShowAllCommand,
    AverageCommand,
    TopperCommand,
)


class InterpreterError(Exception):
    pass


class Interpreter:
    def __init__(self):
       
        self.students = {}

    def run(self, command_list):
        for command in command_list:
            self.execute(command)

    def execute(self, command):
        if isinstance(command, AddStudentCommand):
            self.execute_add(command)
        elif isinstance(command, ShowStudentCommand):
            self.execute_show(command)
        elif isinstance(command, ShowAllCommand):
            self.execute_show_all(command)
        elif isinstance(command, AverageCommand):
            self.execute_average(command)
        elif isinstance(command, TopperCommand):
            self.execute_topper(command)
        else:
            raise InterpreterError(f"Unknown command type: {type(command)}")

    def execute_add(self, command):
        if command.marks < 0:
            raise InterpreterError(
                f"Interpreter Error (line {command.line}): Marks cannot be "
                f"negative (got {command.marks})."
            )
        if command.marks > 100:
            raise InterpreterError(
                f"Interpreter Error (line {command.line}): Marks cannot be "
                f"greater than 100 (got {command.marks})."
            )

        self.students[command.name] = command.marks
        print(f"Student {command.name} added with marks {command.marks}.")

    def execute_show(self, command):
        if command.name not in self.students:
            raise InterpreterError(
                f"Interpreter Error (line {command.line}): Student "
                f"'{command.name}' not found. Add them first using ADD STUDENT."
            )
        marks = self.students[command.name]
        print(f"{command.name} -> {marks} marks")

    def execute_show_all(self, command):
        if len(self.students) == 0:
            print("No students added yet.")
            return

        for name, marks in self.students.items():
            print(f"{name} -> {marks} marks")

    def execute_average(self, command):
        if len(self.students) == 0:
            raise InterpreterError(
                f"Interpreter Error (line {command.line}): Cannot calculate "
                f"average - no students added yet."
            )
        total = sum(self.students.values())
        average = total / len(self.students)
        print(f"Class Average: {average}")

    def execute_topper(self, command):
        if len(self.students) == 0:
            raise InterpreterError(
                f"Interpreter Error (line {command.line}): Cannot find topper "
                f"- no students added yet."
            )
        topper_name = max(self.students, key=self.students.get)
        topper_marks = self.students[topper_name]
        print(f"Topper: {topper_name} with {topper_marks} marks")
