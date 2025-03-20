import pytest
from src.logic.logic import Logica  # Asegúrate de que esta ruta sea correcta

class TestLogica:
    def setup_method(self):
        self.logica = Logica()
    
    def test_AND(self):
        """Verifica la tabla de verdad de AND"""
        assert self.logica.AND(True, True) is True
        assert self.logica.AND(True, False) is False
        assert self.logica.AND(False, True) is False
        assert self.logica.AND(False, False) is False
    
    def test_OR(self):
        """Verifica la tabla de verdad de OR"""
        assert self.logica.OR(True, True) is True
        assert self.logica.OR(True, False) is True
        assert self.logica.OR(False, True) is True
        assert self.logica.OR(False, False) is False
    
    def test_NOT(self):
        """Verifica la tabla de verdad de NOT"""
        assert self.logica.NOT(True) is False
        assert self.logica.NOT(False) is True
    
    def test_XOR(self):
        """Verifica la tabla de verdad de XOR"""
        assert self.logica.XOR(True, True) is False
        assert self.logica.XOR(True, False) is True
        assert self.logica.XOR(False, True) is True
        assert self.logica.XOR(False, False) is False
    
    def test_NAND(self):
        """Verifica la tabla de verdad de NAND"""
        assert self.logica.NAND(True, True) is False
        assert self.logica.NAND(True, False) is True
        assert self.logica.NAND(False, True) is True
        assert self.logica.NAND(False, False) is True
    
    def test_NOR(self):
        """Verifica la tabla de verdad de NOR"""
        assert self.logica.NOR(True, True) is False
        assert self.logica.NOR(True, False) is False
        assert self.logica.NOR(False, True) is False
        assert self.logica.NOR(False, False) is True
    
    def test_XNOR(self):
        """Verifica la tabla de verdad de XNOR"""
        assert self.logica.XNOR(True, True) is True
        assert self.logica.XNOR(True, False) is False
        assert self.logica.XNOR(False, True) is False
        assert self.logica.XNOR(False, False) is True
    
    def test_implicacion(self):
        """Verifica la tabla de verdad de la implicación"""
        assert self.logica.implicacion(True, True) is True
        assert self.logica.implicacion(True, False) is False
        assert self.logica.implicacion(False, True) is True
        assert self.logica.implicacion(False, False) is True
    
    def test_bi_implicacion(self):
        """Verifica la tabla de verdad de la bi-implicación"""
        assert self.logica.bi_implicacion(True, True) is True
        assert self.logica.bi_implicacion(True, False) is False
        assert self.logica.bi_implicacion(False, True) is False
        assert self.logica.bi_implicacion(False, False) is True
