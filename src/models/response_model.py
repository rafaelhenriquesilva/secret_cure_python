from src.models.form_model import Question, Answer
class ResponseForm:
    def __init__(self, questionCorrects: list[Question], filtered_question: list[Question]):
        self.questionCorrects = questionCorrects
        self.filtered_question = filtered_question

    def __getitem__(self, key):
        if key == 'questionCorrects':
            return self.questionCorrects
        elif key == 'filtered_question':
            return self.filtered_question
        else:
            raise KeyError(f"Chave inválida: {key}")   