def es_palindromo(self, texto):
        class Magic:
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

# Ejemplo de uso
magic = Magic()
print(magic.es_palindromo("Anita lava la tina"))  # True
print(magic.es_palindromo("Hola mundo"))  # False
print(magic.es_palindromo("Reconocer"))  # True
        pass
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        pass