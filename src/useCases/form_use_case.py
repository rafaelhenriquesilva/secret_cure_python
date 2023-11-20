from src.models.form_model import FormData, Content, Category, Question
from src.utils.json_util import JSONUtil
# -*- coding: utf-8 -*-

class FormUseCase:
    def convertJsonInFormData(json_name):
        try:
            data_form_json = JSONUtil.loadJson(json_name)

            # Criando instâncias das classes do formulario
            categories = [Category(category['title'], category['api_name'], category['text'], category['position']) for category in data_form_json['categories']]
            contents = [Content(content['title'], content['text'], content['category']) for content in data_form_json['contents']]
            questions = [Question(question['text'], question['correct_answer_id'], question['category'], question['answers']) for question in data_form_json['questions']]

            form_data = FormData(categories, contents, questions)

            return form_data
        except Exception as e:
            print("Erro ao atualizar os dados dos usuários", e)

    def showCategories(categories: list[Category]):
        print('\nEscolha uma categoria para iniciar os estudos!')
        for category in categories:
            print('\n{} - {}\n'.format(category.position, category.title))


    def getCategoryByPosition(categories: list[Category], position):
        filtered_category = [category for category in categories if category['position'] == position]
        return filtered_category
    
    def getContentByCategory(contents: list[Content], category: str):
          filtered_content = [content for content in contents if content['category'] == category]
          return filtered_content
    
    def showContents(contents: list[Content], category):
        print('\nEstude com foco sobre a categoria: {}'.format(category))
        for content in contents:
            print('\n\n{} - {}\n\n'.format(content.title, content.text))

        

    


