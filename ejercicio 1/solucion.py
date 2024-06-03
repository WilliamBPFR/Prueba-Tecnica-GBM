def determinar_palindromo(input: str) -> bool:
    # Aqui lo que se hace es comparar si la palabra es igual a la palabra invertida.
    # Se convierte a minuscula para que no haya problemas de comparacion
    # Se usa slicing para invertir la palabra (input[::-1])
    return input.lower() == input[::-1].lower()

if __name__ == "__main__":
    print(determinar_palindromo("Ana"))