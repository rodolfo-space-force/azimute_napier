import math

def calcular_azimutes(latitude, inclinacao):
    """
    Calcula os azimutes possíveis (prógrado e retrógrado) para uma determinada latitude e inclinação orbital.
    """
    # Checagem de viabilidade física
    if abs(inclinacao) < abs(latitude):
        raise ValueError(f"Inclinação {inclinacao:.2f}° impossível a partir da latitude {latitude:.2f}°.")

    lat_rad = math.radians(latitude)
    inc_rad = math.radians(inclinacao)

    # Caso especial: inclinação = latitude
    if abs(inclinacao - abs(latitude)) < 1e-6:
        return 90.0, 270.0  # Leste e oeste

    # Cálculo do ângulo com base na fórmula
    cos_azimute = math.cos(inc_rad) / math.cos(lat_rad)

    # Limita o valor para evitar domínio inválido na função acos
    cos_azimute = max(-1.0, min(1.0, cos_azimute))

    az = math.degrees(math.acos(cos_azimute))

    # Retorna ambos os possíveis azimutes (prógrado e retrógrado)
    return az, 360 - az


def direcao_cardinal(azimute):
    """
    Traduz o azimute em uma direção cardinal aproximada.
    """
    setores = [
        (22.5, "norte"),
        (67.5, "nordeste"),
        (112.5, "leste"),
        (157.5, "sudeste"),
        (202.5, "sul"),
        (247.5, "sudoeste"),
        (292.5, "oeste"),
        (337.5, "noroeste"),
        (360.0, "norte")
    ]
    for limite, direcao in setores:
        if azimute < limite:
            return direcao
    return "norte"  # fallback


if __name__ == "__main__":
    print("Cálculo do Azimute de Lançamento Orbital – OPERACIONAL\n")

    # Entrada do usuário
    latitude = float(input("Insira a latitude da base de lançamento (em graus): "))
    inclinacao = float(input("Insira a inclinação orbital desejada (em graus): "))

    # Cálculo
    try:
        az_prógrado, az_retrógrado = calcular_azimutes(latitude, inclinacao)

        print("\nAzimutes operacionais possíveis:")
        print(f"Azimute prógrado (rumo sul):   {az_prógrado:.2f}° ({direcao_cardinal(az_prógrado)})")
        print(f"Azimute retrógrado (rumo norte): {az_retrógrado:.2f}° ({direcao_cardinal(az_retrógrado)})")

    except ValueError as e:
        print(str(e))
