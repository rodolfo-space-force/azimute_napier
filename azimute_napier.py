import math

def azimute_operacional(latitude, inclinacao):
    lat = latitude
    inc = inclinacao

    # Verificação física – inclinação não pode ser menor que a latitude (sem manobra orbital)
    if inc < abs(lat):
        raise ValueError(
            f"Inclinação {inc:.2f}° impossível a partir da latitude {abs(lat):.2f}°."
        )

    # Caso especial: inclinação ≈ latitude → lançamento exato para leste
    if abs(inc - abs(lat)) < 1e-6:
        return 90.0

    lat_rad = math.radians(lat)
    inc_rad = math.radians(inc)

    cos_theta = math.cos(inc_rad) / math.cos(lat_rad)
    cos_theta = max(-1.0, min(1.0, cos_theta))  # evita domínio inválido
    theta = math.degrees(math.acos(cos_theta))

    if inc <= 90:
        # Órbita prógrada
        return theta
    else:
        # Órbita retrógrada: aplicar política operacional por hemisfério
        if lat >= 0:
            return 180 - theta  # Hemisfério Norte → lança para sul-sudoeste
        else:
            return 180 + theta  # Hemisfério Sul → lança para noroeste


def direcao(az):
    if az < 67.5:
        return "nordeste"
    elif az < 112.5:
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
    print("\n Cálculo do Azimute de Lançamento Orbital\n")

    try:
        lat = float(input("Insira a latitude da base de lançamento (em graus): "))
        inc = float(input("Insira a inclinação orbital desejada (em graus): "))

        az = azimute_operacional(lat, inc)
        print(f"\n Azimute operacional calculado: {az:.2f}° (em direção {direcao(az)})")

    except ValueError as e:
        print(f"\n Erro: {e}")
