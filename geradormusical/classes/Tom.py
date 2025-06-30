from ..consts import *
import random

# Define um tom da música, ou seja, uma nota e a sua oitava

class Tom:
    def __init__(self):
        self.nota = NOTAS['C']  # default
        self.oitava = OITAVAS['Oitava C-1']  # default

    def set_nota(self, nota):
        if nota not in NOTAS.values():
            raise ValueError("Nota inválida")
        self.nota = nota
    
    def set_oitava(self, oitava):
        if oitava not in OITAVAS.values():
            raise ValueError("Oitava inválida")
        self.oitava = oitava

    def obter_valor_midi(self):
        return self.nota + self.oitava
    
    def randomize_nota(self):
        notas = list(NOTAS.values())
        self.set_nota(random.choice(notas))