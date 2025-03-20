import pytest
from src.strings.strings import Strings  # Asegúrate de que esta ruta sea correcta

class TestStrings:
    def setup_method(self):
        self.strings = Strings()
    
    def test_es_palindromo(self):
        casos = [
            ("oso", True),
            ("neuquen", True),
            ("La ruta natural", True),
            ("elefante", False),
            ("montaña", False),
            ("", True)
        ]
        for palabra, esperado in casos:
            resultado = self.strings.es_palindromo(palabra)
            assert resultado == esperado
    
    def test_invertir_cadena(self):
        casos = [
            ("perro", "orrep"),
            ("Guitarra", "arratiuG"),
            ("montaña", "añaotnom"),
            ("", ""),
            ("z", "z")
        ]
        for cadena, esperado in casos:
            resultado = self.strings.invertir_cadena(cadena)
            assert resultado == esperado
    
    def test_contar_vocales(self):
        casos = [
            ("elefante", 4),
            ("murciélago", 5),
            ("sky", 0),
            ("Oasis", 3),
            ("", 0)
        ]
        for cadena, esperado in casos:
            resultado = self.strings.contar_vocales(cadena)
            assert resultado == esperado
    
    def test_contar_consonantes(self):
        casos = [
            ("guitarra", 5),
            ("elefante", 4),
            ("aiueo", 0),
            ("Bicicleta", 6),
            ("", 0)
        ]
        for cadena, esperado in casos:
            resultado = self.strings.contar_consonantes(cadena)
            assert resultado == esperado
    
    def test_es_anagrama(self):
        casos = [
            ("amor", "roma", True),
            ("radar", "ardar", False),
            ("perro", "roper", True),
            ("escuchar", "chacurse", True),
            ("casa", "saco", False),
            ("tigre", "giter", True)
        ]
        for palabra1, palabra2, esperado in casos:
            resultado = self.strings.es_anagrama(palabra1, palabra2)
            assert resultado == esperado
    
    def test_contar_palabras(self):
        casos = [
            ("El sol brilla", 3),
            ("El agua es transparente", 4),
            ("  caminando por la calle    ", 4),
            ("", 0)
        ]
        for frase, esperado in casos:
            resultado = self.strings.contar_palabras(frase)
            assert resultado == esperado
    
    def test_palabras_mayus(self):
        casos = [
            ("buenos dias", "Buenos Dias"),
            ("la montaña es alta", "La Montaña Es Alta"),
            ("Hola Mundo", "Hola Mundo"),
            ("  caminando  por  la  calle  ", "  Caminando  Por  La  Calle  "),
            ("", "")
        ]
        for frase, esperado in casos:
            resultado = self.strings.palabras_mayus(frase)
            assert resultado == esperado
    
    def test_eliminar_espacios_duplicados(self):
        casos = [
            ("Hola  mundo", "Hola mundo"),
            ("  caminando   por   la   ciudad  ", " caminando por la ciudad "),
            ("Buenos días", "Buenos días"),
            ("", "")
        ]
        for frase, esperado in casos:
            resultado = self.strings.eliminar_espacios_duplicados(frase)
            assert resultado == esperado
    
    def test_es_numero_entero(self):
        casos = [
            ("789", True),
            ("-321", True),
            ("56.78", False),
            ("abcd", False)
        ]
        for numero, esperado in casos:
            resultado = self.strings.es_numero_entero(numero)
            assert resultado == esperado
