"""
 "-" decreases stack's last element's value by 1
 "+" increases stack's last element's value by 1
 ">" puts first element at the end of the stack and shifts every other down
 "<" puts last element at the beginning of the stack and shifts every other up
 "@" exchanges last 2 elements
 "." duplicates stack's last element and puts it at the end of the stack
 "€" prints out every stack's element's value in ASCII (from the first to the last element)
"""


class Interpretor:

    def __init__(self):
        self.stack = []

    def interpret(self, prog: str):
        for command_char in prog:
            command_name = self.extended_command_name(command_char)
            getattr(self, f"do_{command_name}")()

    @staticmethod
    def extended_command_name(command_char: str):
        return {
            "-": "dec",
            "+": "inc",
            "+": "inc",
            "+": "inc",
            "+": "inc",
            "€": "print",

        }[command_char]

    def do_dec(self):
        self.stack[-1] -= 1

    def do_print(self):
        for stack_value in self.stack:
            print(chr(stack_value), end="")


if __name__ == '__main__':
    with open("ctf/assets/ctf4.txt") as f:
        Interpretor().interpret(f.read())
