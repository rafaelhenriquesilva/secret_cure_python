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
    def __init__(self, text, answer_id, vowel=any):
        self.text = text
        self.answer_id = answer_id
        self.vowel = vowel

    def __getitem__(self, key):
        if key == 'answer_id':
            return self.answer_id
        elif key == 'text':
            return self.text
        elif key == 'vowel':
            return self.vowel
        else:
            raise KeyError(f"Chave inválida: {key}")     
        
    def set_vowel(self, vowel):
        self.vowel = vowel    

class Question:
    def __init__(self, text, correct_answer_id, category, answers):
        self.text = text
        self.correct_answer_id = correct_answer_id
        self.category = category
        self.answers = [Answer(ans['text'], ans['id']) for ans in answers]

    def __getitem__(self, key):
        if key == 'correct_answer_id':
            return self.correct_answer_id
        elif key == 'text':
            return self.text
        elif key == 'category':
            return self.category
        elif key == 'answers':
            return self.answers                
        else:
            raise KeyError(f"Chave inválida: {key}")    

class FormData:
    def __init__(self, categories, contents, questions):
        self.categories = categories
        self.contents = contents
        self.questions = questions

    def __getitem__(self, key):
        if key == 'categories':
            return self.categories
        elif key == 'contents':
            return self.contents
        elif key == 'questions':
            return self.questions
        else:
            raise KeyError(f"Chave inválida: {key}")   
