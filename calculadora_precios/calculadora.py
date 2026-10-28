"""Calculadora de precios.

Permite calcular un precio con IVA, aplicar un descuento y obtener
el precio final aplicando ambos.
"""

IVA_POR_DEFECTO = 21


def calcular_precio_con_iva(precio, iva=IVA_POR_DEFECTO):
    """Calcula el precio con IVA incluido.

    :param precio: Precio base sin IVA, en euros.
    :type precio: float
    :param iva: Porcentaje de IVA a aplicar (por defecto 21).
    :type iva: float
    :return: Precio con IVA incluido.
    :rtype: float
    :raises ValueError: Si el precio o el IVA son negativos.
    """
    if precio < 0 or iva < 0:
        raise ValueError("El precio y el IVA no pueden ser negativos")
    return precio * (1 + iva / 100)


def aplicar_descuento(precio, descuento):
    """Aplica un descuento porcentual a un precio.

    :param precio: Precio original, en euros.
    :type precio: float
    :param descuento: Porcentaje de descuento, entre 0 y 100.
    :type descuento: float
    :return: Precio con el descuento aplicado.
    :rtype: float
    :raises ValueError: Si el precio es negativo o el descuento
        no está entre 0 y 100.
    """
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if not 0 <= descuento <= 100:
        raise ValueError("El descuento debe estar entre 0 y 100")
    return precio * (1 - descuento / 100)


def calcular_precio_final(precio, descuento, iva=IVA_POR_DEFECTO):
    """Calcula el precio final aplicando primero el descuento y luego el IVA.

    :param precio: Precio base sin IVA, en euros.
    :type precio: float
    :param descuento: Porcentaje de descuento, entre 0 y 100.
    :type descuento: float
    :param iva: Porcentaje de IVA a aplicar (por defecto 21).
    :type iva: float
    :return: Precio final con descuento e IVA.
    :rtype: float
    :raises ValueError: Si algún dato no es válido.
    """
    return calcular_precio_con_iva(aplicar_descuento(precio, descuento), iva)


def main():
    """Ejecuta la calculadora en modo interactivo por consola."""
    print("Calculadora de precios")
    print("1. Calcular precio con IVA")
    print("2. Aplicar descuento")
    print("3. Calcular precio final (descuento + IVA)")
    opcion = input("Elige una opción: ")

    try:
        precio = float(input("Introduce el precio: "))
        if opcion == "1":
            print(f"Precio con IVA: {calcular_precio_con_iva(precio):.2f} €")
        elif opcion == "2":
            descuento = float(input("Descuento (%): "))
            print(f"Precio con descuento: {aplicar_descuento(precio, descuento):.2f} €")
        elif opcion == "3":
            descuento = float(input("Descuento (%): "))
            print(f"Precio final: {calcular_precio_final(precio, descuento):.2f} €")
        else:
            print("Opción no válida")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()