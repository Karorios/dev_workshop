class Magic:
    """
    Clase con métodos para realizar operaciones de lógica booleana y algoritmos.
    """

    def AND(self, a, b):
        """
        Implementa la operación lógica AND con números.
        Todo número distinto de 0 se considera True y el 0 se considera False.

        Args:
            a (int): Primer número
            b (int): Segundo número

        Returns:
            int: 1 si ambos números son distintos de 0 (True AND True), 0 en caso contrario
        """
        return int(bool(a) and bool(b))

# Ejemplo de uso
magic = Magic()
print(magic.AND(5, 3))  # 1
print(magic.AND(0, 7))  # 0
print(magic.AND(8, 0))  # 0
print(magic.AND(0, 0))  # 0
