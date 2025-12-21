import math

def azimute_operacional(latitude, inclinacao):
    # Limite físico
    if inclinacao < abs(latitude):
        raise ValueError(
            f"Inclinação {inclinacao:.2f}° impossível a partir da latitude {abs(latitude):.2f}°."
        )

    # Caso especial: inclinação mínima direta
    if abs(inclinacao - abs(latitude)) < 1e-6:
        return 90.0  # Leste puro

    lat_rad = math.radians(latitude)
    inc_rad = math.radians(inclinacao)

    # Ângulo geométrico auxiliar (NÃO é azimute)
    cos_theta = math.cos(inc_rad) / math.cos(lat_rad)
    cos_theta = max(-1.0, min(1.0, cos_theta))
    theta = math.degrees(math.acos(cos_theta))

    if inclinacao <= 90:
        # Prógrada
        return theta
    else:
        # Retrógrada OPERACIONAL (SSO)
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
    print("\n🛰️  Cálculo do Azimute de Lançamento Orbital – OPERACIONAL\n")

    lat = float(input("Insira a latitude da base de lançamento (em graus): "))
    inc = float(input("Insira a inclinação orbital desejada (em graus): "))

    az = azimute_operacional(lat, inc)
    print(f"\n✅ Azimute operacional calculado: {az:.2f}° (em direção {direcao(az)})")
