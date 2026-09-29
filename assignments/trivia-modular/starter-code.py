"""Código inicial para o Jogo de Trivia Modular."""


questions = [
    {
        "question": "Qual palavra-chave cria uma função em Python?",
        "options": {"A": "func", "B": "def", "C": "function", "D": "define"},
        "answer": "B",
        "category": "Python",
    },
    {
        "question": "Qual estrutura armazena pares de chave e valor?",
        "options": {"A": "lista", "B": "tupla", "C": "dicionário", "D": "conjunto"},
        "answer": "C",
        "category": "Python",
    },
    {
        "question": "Quantos lados tem um hexágono?",
        "options": {"A": "cinco", "B": "seis", "C": "sete", "D": "oito"},
        "answer": "B",
        "category": "Conhecimentos gerais",
    },
    {
        "question": "Qual planeta é conhecido como planeta vermelho?",
        "options": {"A": "Vênus", "B": "Júpiter", "C": "Marte", "D": "Saturno"},
        "answer": "C",
        "category": "Ciência",
    },
    {
        "question": "Qual destes é um tipo de dado booleano?",
        "options": {"A": "True", "B": "Text", "C": "Number", "D": "List"},
        "answer": "A",
        "category": "Python",
    },
]


def show_question(question):
    """Exiba uma pergunta, sua categoria e suas alternativas."""
    pass


def get_answer(question):
    """Solicite e devolva uma alternativa válida."""
    pass


def play_round(question, score):
    """Exiba uma pergunta, processe a resposta e devolva o novo placar."""
    pass


def main():
    score = 0

    for question in questions:
        score = play_round(question, score)

    print(f"Você acertou {score} de {len(questions)} perguntas.")


if __name__ == "__main__":
    main()