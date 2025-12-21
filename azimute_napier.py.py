# Rodolfo Milhomem – github.com/rodolfo-space-force

import math

def calcular_azimute(lat, inclinacao):
    """
    Calcula o azimute de lançamento (graus) com base na latitude e inclinação desejada.
    Inclinações > 90° são tratadas como retrógradas.
    Inclinações < latitude são fisicamente impossíveis com lançamento direto.
    """
    lat_rad = math.radians(lat)
    inc_rad = math.radians(inclinacao)

    # Verificação de limite físico
    limite = math.cos(inc_rad) / math.cos(lat_rad)
    if abs(limite) > 1:
        raise ValueError(
            f"️ Inclinação de {inclinacao:.2f}° não é possível a partir da latitude {abs(lat):.2f}° "
            f"sem manobra orbital. Inclinação mínima possível: {abs(lat):.2f}°"
        )

    # Caso especial: inclinação ≈ latitude (lançamento exato para leste)
    if abs(abs(inclinacao) - abs(lat)) < 1e-2:
        return 90.0  # azimute exato para leste

    # Cálculo normal do ângulo
    angulo = math.degrees(math.acos(limite))

    # Órbita prógrada ou retrógrada
    if inclinacao <= 90:
        azimute = angulo
    else:
        azimute = 180 + angulo  # direção retrógrada segura

    return azimute


def interpretar_direcao(az):
    """
    Interpreta a direção geográfica aproximada com base no azimute.
    """
    if az < 22.5 or az >= 337.5:
        return "norte"
    elif az < 67.5:
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
    print("\nCálculo do Azimute de Lançamento Orbital\n")

    try:
        lat = float(input("Insira a latitude da base de lançamento (em graus): "))
        inclinacao = float(input("Insira a inclinação orbital desejada (em graus): "))

        az = calcular_azimute(lat, inclinacao)
        direcao = interpretar_direcao(az)

        print(f"\n Azimute calculado: {az:.2f}° (em direção {direcao})")

    except ValueError as e:
        print(f"\n{e}")
