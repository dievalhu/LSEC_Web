import re
from typing import List, Optional
from models.Q0 import Q0
from models.Q1 import Q1
from models.Q2 import Q2
from models.Token import Token, Tipos

class Lexer:

    def __init__(self, text_to_translate: str = ""):
        self.text_to_translate = text_to_translate
        self.q0 = None
        self.q1 = None
        self.q2 = None
        self.tokens: List[Token] = []

    def lexer_analyzer(self):
        word_acum = ""
        characters = list(self.text_to_translate + " ")

        for i, char in enumerate(characters):
            #print(f"Análisis del caracter {i}: '{char}'")
            if i == 0:
                self.q0 = Q0(char)
                if not self.q0.is_valid:
                    raise Exception(f"The text is not admitted by the automaton (Error Q0) for '{char}'")
                word_acum += char
            else:
                self.q1 = Q1(char)
                if not self.q1.is_valid:
                    raise Exception(f"The text is not admitted by the automaton (Error Q1) for '{char}'")
                if self.q1.string_input != ' ':
                    word_acum += char
                else:
                    self.q2 = Q2(self.q0.is_valid, self.q1.is_valid)
                    if not self.q2.is_valid:
                        raise Exception(f"The text is not admitted by the automaton (Error Q2) for '{char}'")
                    #print(f"Enviando '{word_acum}' al lexer.")
                    self.lex(word_acum)
                    word_acum = ""

    def lex(self, input_str: str):
        # Verifica si el input_str es vacío o solo contiene espacios
        if not input_str.strip():
            return

        matched = False
        for token_type in Tipos:
            pattern = token_type.value     
            if re.match(pattern, input_str):
                token = Token(tipo=token_type, valor=input_str)  # Aquí, `token_type` debe ser una instancia de Tipos.
                self.tokens.append(token)
                matched = True
                break

        if not matched:
            raise RuntimeError(f"Se encontró un token inválido: '{input_str}'.")





