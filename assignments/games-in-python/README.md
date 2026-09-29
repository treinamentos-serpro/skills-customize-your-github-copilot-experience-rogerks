
# 📘 Assignment: Jogo da Forca

## 🎯 Objective

Construa um jogo da forca em Python para praticar manipulação de strings, listas, entrada de dados, condicionais e loops. O jogador deve descobrir uma palavra oculta antes de esgotar as tentativas. Teste 123.

## 📝 Tasks

### 🛠️ Preparar a Palavra e Registrar Palpites

#### Descrição
Crie a estrutura inicial do jogo: escolha uma palavra aleatoriamente de uma lista predefinida, mostre suas letras ocultas e permita que o jogador informe palpites de uma letra.

#### Requisitos
O programa concluído deve:

- Selecionar uma palavra aleatoriamente de uma lista com pelo menos cinco palavras.
- Exibir uma posição oculta para cada letra da palavra, por exemplo, `_ _ _ _`.
- Solicitar palpites de uma letra e revelar todas as posições correspondentes quando o palpite estiver correto.
- Registrar as letras já escolhidas para que o jogador possa acompanhar seus palpites.

### 🛠️ Controlar a Partida e Exibir o Resultado

#### Descrição
Adicione o controle de tentativas e as condições de encerramento para completar uma partida jogável do início ao fim.

#### Requisitos
O programa concluído deve:

- Começar com um número definido de tentativas incorretas disponíveis.
- Reduzir as tentativas restantes quando o jogador errar e exibir quantas ainda restam.
- Encerrar a partida quando todas as letras forem reveladas ou quando as tentativas acabarem.
- Exibir uma mensagem de vitória ou derrota; em caso de derrota, revelar a palavra correta.