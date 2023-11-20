import sys
import os

# Obtendo o caminho absoluto do diretório atual (__tests__) e adicionando o diretório pai (SecretCure) ao PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.useCases.form_use_case import FormUseCase
from src.useCases.question_use_case import QuestionUseCase
from src.models.form_model import FormData, Category, Content

def test_get_question_by_category():
    fake_form: FormData = FormUseCase.convertJsonInFormData('fake_form.json')

    assert len(fake_form.categories) > 0

    category: Category = FormUseCase.getCategoryByPosition(fake_form.categories, 1)[0]

    assert category.position == 1
    assert category.api_name != ''    

    question: list[Content] = QuestionUseCase.getQuestionsByCategory(fake_form.questions, category.api_name)

    assert len(question) > 0

   
