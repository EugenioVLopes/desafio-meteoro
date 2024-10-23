# Meteor Challenge

## Descrição

Este projeto analisa uma imagem para contar o número de estrelas, meteoros e determinar quantos meteoros caem na água sem serem bloqueados por montanhas.

## Resultados

- Número de Estrelas: 315
- Número de Meteoros: 328
- Meteoros caindo na Água: 105

## Como obtive esse resultados?

Para contar as estrelas, foi utilizado o seguinte método:

- Carregamento da Imagem: Primeiramente, a imagem foi carregada no código utilizando a biblioteca Pillow, que permite manipular e analisar imagens em Python.

- Análise dos Pixels: Em seguida, cada pixel da imagem foi verificado individualmente. Em relação ao valor retornado das cores vi que também era retornado o valor do canal de transparÊncia (Alpha), então também fiz a verificação desse valor.

## Contagem do Número de Estrelas

Identificando estrelas: Para identificar as estrelas, procurei por pixels que correspondem à cor branca pura conforme intruido pelo desafio. A cor branca na imagem é representada pelo valor RGB (255, 255, 255) e possui um canal de transparência (Alpha) de 255. Assim, procurei por pixels com esses valores (255, 255, 255, 255).

Contagem das Estrelas: A cada vez que um pixel branco era encontrado, ele era considerado como uma estrela, e o contador de estrelas era incrementado.

Resultado: Foram contadas 315 estrelas na imagem.

## Contagem do Número de Meteoros

A contagem dos meteoros foi realizada de maneira semelhante:

Identificação dos Meteoros: Neste caso, os meteoros foram identificados pela cor vermelha pura, que na imagem é representada pela combinação de valores RGB (255, 0, 0), ou seja, o componente vermelho está no máximo, enquanto o verde e o azul estão zerados. Assim, procurei por pixels com o valor (255, 0, 0, 255).

## Contagem dos Meteoros:

Cada vez que um pixel vermelho era encontrado, ele era contabilizado como um meteoro, e o contador de meteoros era incrementado.

Resultado: Foram identificados 328 meteoros na imagem.

## Contagem dos Meteoros Caindo na Água

Para determinar quantos meteoros caem diretamente na água, sem serem bloqueados pelas montanhas, o processo foi mais detalhado:

Para verificar se um meteoro caía na água, o código foi desenhado para analisar todos os pixels abaixo de um meteoro.
Ao encontrar um meteoro (pixel vermelho), o algoritmo iniciava uma verificação na coluna de pixels abaixo até encontrar a cor azul (representando a água) ou a cor preta (representando o solo).
Se encontrasse um pixel azul primeiro, o meteoro era considerado como caindo na água e o contador era incrementado. Caso encontrasse um pixel preto, o meteoro era bloqueado pela montanha e não contava como caindo na água.

Resultado: Foram contados 105 meteoros que caem diretamente na água.

## Como Executar o Projeto

### Pré-requisitos

Python 3.x deve estar instalado na sua máquina.
A biblioteca Pillow deve estar instalada. Você pode instalá-la executando pip install pillow no terminal.

**Execute o Código:**

- No terminal, dentro do diretório do projeto, execute:
  ```bash
  python meteor_code.py
  ```
