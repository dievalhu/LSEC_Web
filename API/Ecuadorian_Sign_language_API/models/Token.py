# models/Token.py

from enum import Enum

class Tipos(Enum):
    DIGITO = r"^[0-9]+$"            
    LETRA = r"^[a-zA-Záéíóúñ]$"
    PALABRA = r"^[a-zA-Z0-9áéíóúñ]+$"

class Token:
    def __init__(self, tipo: Tipos, valor: str):
        self.tipo = tipo         
        self.valor = valor

    def __str__(self):
        return f"({self.tipo.name}: {self.valor})"


