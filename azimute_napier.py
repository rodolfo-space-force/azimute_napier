#Rodolfo Milhomem
#https://github.com/rodolfo-space-force/

import math

def azimute_operacional(latitude, inclinacao):
    lat = latitude
    inc = inclinacao

    # Limite físico
    if inc < abs(lat):
        raise ValueError(
            f"Inclinação {inc:.2f}° impossível a partir da latitude {abs(lat):.2f}°."
        )

    # Caso especial: inclinação mínima direta
    if abs(inc - abs(lat)) < 1e-6:
        return 90.0  # Leste puro

    lat_rad = math.radians(lat)
    inc_rad = math.radians(inc)

    cos_theta = math.cos(inc_rad) / math.cos(lat_rad)
    cos_theta = max(-1.0, min(1.0, cos_theta))

    theta = math.degrees(math.acos(cos_theta))

    if inc <= 90:
        # Prógrada
        return theta
    else:
        # Retrógrada OPERACIONAL (Vandenberg / SSO)
        return 180 + (theta - 90)


def direcao(az):
    if az < 112.5:
        return "leste"
    elif az < 157.5:
        return "sudeste"
    elif az < 202.5:
        return "sul"
    elif az < 247.5:
        return "sudoeste"
    elif az < 292.5:
        return "oeste"
    else:
        return "noroeste"


if __name__ == "__main__":
    print("\nCálculo do Azimute de Lançamento Orbital – OPERACIONAL\n")

    lat = float(input("Insira a latitude da base de lançamento (em graus): "))
    inc = float(input("Insira a inclinação orbital desejada (em graus): "))

    az = azimute_operacional(lat, inc)

    print(f"\nAzimute operacional calculado: {az:.2f}° (em direção {direcao(az)})")


# Licença
#Este projeto está licenciado sob a **Licença MIT**.  
#Você pode usar, modificar e redistribuir este código livremente, **desde que mencione o autor original**.
