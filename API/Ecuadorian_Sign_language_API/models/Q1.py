# models/Q1.py

import re

class Q1:

    def __init__(self, string_input: str = None):
        self.string_input = string_input
        self.is_valid = True
        if self.string_input:
            self.analyze_q1()

    def analyze_q1(self):
        self.is_valid = bool(re.match(r"[a-zA-Z0-9áéíóúñ .]", self.string_input))

