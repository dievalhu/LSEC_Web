# models/Q0.py

import re

class Q0:

    def __init__(self, string_input: str = None):
        self.string_input = string_input
        self.is_valid = False
        if self.string_input:
            self.analyze_q0()

    def analyze_q0(self):
        self.is_valid = bool(re.match(r"[a-zA-z0-9áéíóúñ]", self.string_input))
