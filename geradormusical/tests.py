from django.test import TestCase
from .classes.Instrumento import Instrumento
from .classes.Tom import Tom
from .consts import *

class InstrumentoTestCase(TestCase):
    def setUp(self):
        self.instrumento = Instrumento()

    def test_instrumento_inicial(self):
        self.assertEqual(self.instrumento.obter_valor(), INSTRUMENTOS['Telefone Tocando'])

    def test_trocar_instrumento(self):
        self.instrumento.trocar()
        self.assertEqual(self.instrumento.obter_valor(), INSTRUMENTOS['Agogô'])
    
    def test_trocar_instrumento_circular(self):
        for _ in range(len(INSTRUMENTOS)):
            self.instrumento.trocar()
        self.assertEqual(self.instrumento.obter_valor(), INSTRUMENTOS['Telefone Tocando'])

    def test_set_codigo_valido(self):
        self.instrumento.set_codigo(INSTRUMENTOS['Gaita de Foles'])
        self.assertEqual(self.instrumento.obter_valor(), INSTRUMENTOS['Gaita de Foles'])

    def test_set_codigo_invalido(self):
        with self.assertRaises(ValueError):
            self.instrumento.set_codigo(999)  

# testar tom

class TomTestCase(TestCase):
    def setUp(self):
        self.tom = Tom()

    def test_tom_inicial(self):
        self.assertEqual(self.tom.obter_valor_midi(), 48)

    def test_set_tom_valido(self):
        self.tom.set_tom(NOTAS['C'], OITAVAS['Oitava C4'])
        self.assertEqual(self.tom.obter_valor_midi(), 60)

    def test_set_nota_invalida(self):
        with self.assertRaises(ValueError):
            self.tom.set_nota(999)
            
    def test_set_oitava_invalida(self):
        with self.assertRaises(ValueError):
            self.tom.set_oitava(999)

