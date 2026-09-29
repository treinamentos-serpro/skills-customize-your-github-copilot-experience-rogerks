# 📘 Assignment: Jogo de Trivia Modular

## 🎯 Objective

Construa um jogo de perguntas e respostas em Python para praticar funções, listas, dicionários e organização de código. O jogador deverá responder a uma sequência de perguntas, receber feedback e acompanhar sua pontuação.

## 📝 Tasks

### 🛠️ Criar o Banco de Perguntas

#### Descrição
Defina um banco de perguntas usando uma lista de dicionários. Cada pergunta deve conter o enunciado, quatro alternativas, a resposta correta e uma categoria. Em seguida, crie uma função que exiba uma pergunta e suas alternativas.

#### Requisitos
O programa concluído deve:

- Armazenar pelo menos cinco perguntas em uma lista de dicionários.
- Incluir pelo menos duas categorias diferentes de perguntas.
- Representar cada pergunta com um enunciado, quatro alternativas e uma resposta correta.
- Usar uma função para exibir o enunciado e as alternativas de uma pergunta.

### 🛠️ Processar Respostas e Atualizar o Placar

#### Descrição
Adicione funções para validar a resposta do jogador, informar se ele acertou ou errou e atualizar o placar. A entrada deve aceitar somente uma das alternativas disponíveis.

#### Requisitos
O programa concluído deve:

- Solicitar uma resposta para cada pergunta e aceitar as opções `A`, `B`, `C` ou `D`.
- Rejeitar entradas inválidas sem encerrar o programa.
- Comparar a resposta do jogador com a resposta correta sem diferenciar maiúsculas e minúsculas.
- Aumentar a pontuação somente quando o jogador acertar.
- Exibir feedback após cada resposta.

### 🛠️ Executar a Partida Completa

#### Descrição
Combine as funções em um loop principal que percorra todas as perguntas e apresente um resumo ao final da partida.

#### Requisitos
O programa concluído deve:

- Executar todas as perguntas do banco sem repetir código desnecessariamente.
- Manter a pontuação durante toda a partida.
- Exibir a pontuação final no formato `Você acertou X de Y perguntas.`.
- Exibir uma mensagem diferente para pelo menos três faixas de desempenho.
- Permitir que o jogador veja a categoria da pergunta antes de respondê-la.
