# azimute_napier
Calcular o azimute de lançamento de Veículo Lançador.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/topics/python)

O código serve para calcular o azimute de lançamento (ângulo no horizonte em que o foguete deve ser lançado) para atingir uma órbita com determinada inclinação a partir de uma latitude de lançamento.

![Texto alternativo da imagem](inclinacao.png)

Exemplos de dados que você pode inserir

 1. Cabo Canaveral (EUA)

 Latitude: 28.5
 Inclinação desejada: 28.5 (órbita mínima possível desde essa base)
 Resultado esperado: azimute ≈ 90° (lançamento para o leste, alinhado com a rotação da Terra).

---

 2. Guiana Francesa (Centro Espacial de Kourou)

 Latitude: 5.2
 Inclinação desejada: 5.2
 Resultado esperado: azimute ≈ 90° (também puro leste, aproveitando totalmente a rotação da Terra).

---

 3. Alcântara (Brasil)

 Latitude: 2.3
 Inclinação desejada: 0.0 (órbita equatorial perfeita)
 Resultado esperado: azimute ≈ 90° (exatamente para leste, ideal para GEO).
 Quando você digita -2.3, o código entende que está no hemisfério sul, e retorna corretamente o azimute 277.4° que é o usado em missões reais lançadas de Alcântara para órbitas SSO.

Para órbitas equatoriais (ex: GEO):
O sinal da latitude não muda o azimute  = 90° para ambos os hemisférios.

Para órbitas inclinadas (ex: SSO):
O sinal da latitude é determinante, porque ele define o lado do planeta por onde o foguete deve subir para alcançar com segurança a inclinação desejada sem sobrevoar continentes.

---

 4. Vandenberg (Califórnia, EUA)

 Latitude: 34.7
 Inclinação desejada: 98.0 (órbita heliossíncrona / retrógrada)
 Resultado esperado: azimute ≈ ≈190° (lançamento para sul/sudoeste, sobre o Pacífico).

---

 Observações importantes

1. Limite de inclinação mínima: um local de latitude φ não pode lançar para inclinações menores que φ (em órbita prógrada). Exemplo: de Cabo Canaveral (28.5°N), não se pode lançar para 10° de inclinação.
2. Órbitas retrógradas (> 90°): o foguete vai para o oeste (azimute > 180°).
3. Usos práticos:

    Órbitas geoestacionárias → azimute leste (90°).
    Órbitas polares → lançamentos norte ou sul (\~0° ou 180°).

You can reach me at rmilhomem[at]gmail[dot]com or connect on [LinkedIn](https://www.linkedin.com/in/rodolfo-space-force/) for collaborations.


## Licença

Este projeto está licenciado sob a Licença MIT. Você pode usar, modificar e redistribuir este código livremente, desde que mencione o autor original.

[![MIT License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)


