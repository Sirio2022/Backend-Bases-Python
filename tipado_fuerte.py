nombre: str = "Juan Manuel"
edad: int = 49
familia: list = ["Abel", "Gloria", "Obi Wan"]
atributos: dict = {"altura": 1.75, "peso": 70.5, "color_ojos": "marrón"}
programador: bool = True

def imprimir_nombre(nombre_persona: str) -> None:
    print(f"Nombre: {nombre_persona}")

def calcular_potencia(num: int, potencia: int) -> int:
    return num ** potencia

def ordenar_numeros(numeros: list) -> list:
    return sorted(numeros)

def main() -> None:
    imprimir_nombre(nombre)
    print(f"Edad: {edad}")
    print(f"Familia: {', '.join(familia)}")
    print(f"Atributos: {atributos}")
    print(f"Programador: {'Sí' if programador else 'No'}")

    potencia = calcular_potencia(2, 3)
    print(f"2 elevado a 3 es: {potencia}")

    numeros = [5, 2, 9, 1, 5, 6]
    numeros_ordenados = ordenar_numeros(numeros)
    print(f"Números ordenados: {numeros_ordenados}")

if __name__ == "__main__":
    main()