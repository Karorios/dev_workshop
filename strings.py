class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    """

    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).

        Args:
            texto (str): Cadena a verificar

        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")  # Normalizar el texto
        return texto == texto[::-1]  # Compara la cadena con su versión invertida

    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.

        Args:
            texto (str): Cadena para contar vocales

        Returns:
            int: Número de vocales en la cadena
        """
        texto = texto.lower()  # Convertir a minúsculas para simplificar
        vocales = "aeiou"
        return sum(1 for letra in texto if letra in vocales)  # Contar vocales

# Ejemplo de uso
magic = Magic()
print(magic.es_palindromo("Anita lava la tina"))  # True
print(magic.es_palindromo("Hola mundo"))  # False
print(magic.es_palindromo("Reconocer"))  # True

print(magic.contar_vocales("Hola Mundo"))  # 4
print(magic.contar_vocales("Python es genial"))  # 6
