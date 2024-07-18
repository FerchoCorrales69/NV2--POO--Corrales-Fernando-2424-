def calculate_rectangle_area(length: float, width: float) -> float:
    """
    Calcula el área de un rectángulo.

    Parámetros:
    length (float): La longitud del rectángulo.
    width (float): El ancho del rectángulo.

    Retorna:
    float: El área del rectángulo.
    """
    return length * width


def main():
    # Solicitar al usuario la longitud y el ancho del rectángulo
    length = float(input("Ingresa la longitud del rectángulo: "))
    width = float(input("Ingresa el ancho del rectángulo: "))

    # Calcular el área del rectángulo
    area = calculate_rectangle_area(length, width)

    # Determinar si el rectángulo es un cuadrado
    is_square = length == width

    # Mostrar el resultado
    print(f"\nEl área del rectángulo con longitud {length} y ancho {width} es: {area}")

    if is_square:
        print("Este rectángulo es un cuadrado.")
    else:
        print("Este rectángulo no es un cuadrado.")


if __name__ == "__main__":
    main()




