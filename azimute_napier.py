#Rodolfo Milhomem
#https://github.com/rodolfo-space-force/

import math

def calcular_azimute(lat, inclinacao):
    """
    Calcula o azimute de lançamento para atingir uma inclinação orbital desejada,
    considerando direções prógrada e retrógrada.
    """
    lat_rad = math.radians(lat)
    inclinacao_rad = math.radians(inclinacao)

    cos_inclinacao = math.cos(inclinacao_rad)
    cos_lat = math.cos(lat_rad)

    limite = cos_inclinacao / cos_lat

    if abs(limite) > 1.0:
        raise ValueError(f"Inclinação {inclinacao:.2f}° não é possível a partir da latitude {lat:.2f}°.")

    azimute_rad = math.asin(limite)

    # Inclinação ≤ 90° → órbita prógrada (azimute leste)
    # Inclinação > 90° → órbita retrógrada (azimute oeste)
    if inclinacao <= 90:
        azimute = math.degrees(azimute_rad)
    else:
        azimute = 180 - math.degrees(azimute_rad)

    return azimute


if __name__ == "__main__":
    print(" Cálculo do Azimute de Lançamento Orbital\n")

    try:
        latitude = float(input("Insira a latitude da base de lançamento (em graus): "))
        inclinacao = float(input("Insira a inclinação orbital desejada (em graus): "))

        azimute = calcular_azimute(latitude, inclinacao)
        direcao = "leste" if azimute < 90 or azimute == 90 else "oeste"

        print(f"\n Azimute calculado: {azimute:.2f}° (em direção {direcao})")

    except ValueError as e:
        print(f"\n Erro: {e}")

    
# Licença
#Este projeto está licenciado sob a **Licença MIT**.  
#Você pode usar, modificar e redistribuir este código livremente, **desde que mencione o autor original**.
