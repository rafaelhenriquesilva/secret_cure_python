class Category:
    def __init__(self, title, api_name, text, position):
        self.title = title
        self.api_name = api_name
        self.text = text
        self.position = position

    def __getitem__(self, key):
        if key == 'api_name':
            return self.api_name
        elif key == 'title':
            return self.title
        elif key == 'text':
            return self.text
        elif key == 'position':
            return self.position
        else:
            raise KeyError(f"Chave inválida: {key}")        

class Content:
    def __init__(self, title, text, category):
        self.title = title
        self.text = text
        self.category = category

    def __getitem__(self, key):
        if key == 'category':
            return self.category
        elif key == 'title':
            return self.title
        elif key == 'text':
            return self.text
        else:
            raise KeyError(f"Chave inválida: {key}")        

class Answer:
    def __init__(self, text, answer_id):
        self.text = text
        self.id = answer_id

class Question:
    def __init__(self, text, correct_answer_id, category, answers):
        self.text = text
        self.correct_answer_id = correct_answer_id
        self.category = category
        self.answers = [Answer(ans['text'], ans['id']) for ans in answers]

class FormData:
     def __init__(self, categories, contents, questions):
        self.categories = categories
        self.contents = contents
        self.questions = questions
