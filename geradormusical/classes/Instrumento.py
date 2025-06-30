from ..consts import *

# Define um instrumento
# Permite obter seu valor MIDI e trocar para um novo instrumento

class Instrumento:
    def __init__(self):
        self.codigo = INSTRUMENTOS['Telefone tocando']  #default

    def set_codigo(self, codigo):
        if (isinstance(codigo, int) and codigo in INSTRUMENTOS.values()):
            self.codigo = codigo
        else:
            raise ValueError("Valor do instrumento deve ser válido.")

    def obter_valor(self):
        return self.codigo

    def trocar(self):
        '''Troca o instrumento atual pelo próximo na lista de instrumentos de forma circular.'''
        instrumentos = list(INSTRUMENTOS.values())
        index = instrumentos.index(self.codigo)
        self.codigo = instrumentos[(index + 1) % len(instrumentos)]
