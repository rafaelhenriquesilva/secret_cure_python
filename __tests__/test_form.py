import sys
import os

# Obtendo o caminho absoluto do diretório atual (__tests__) e adicionando o diretório pai (SecretCure) ao PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.useCases.form_use_case import FormUseCase
from src.models.form_model import FormData, Category, Content

def test_convert_form_json():
    fake_form: FormData = FormUseCase.convertJsonInFormData('fake_form.json')

    assert len(fake_form.categories) > 0
    assert len(fake_form.contents) > 0
    assert len(fake_form.questions) > 0
    assert len(fake_form.questions[0].answers) > 0

def test_get_category_by_position():
    fake_form: FormData = FormUseCase.convertJsonInFormData('fake_form.json')

    assert len(fake_form.categories) > 0

    category: Category = FormUseCase.getCategoryByPosition(fake_form.categories, 1)[0]

    assert category.position == 1
    assert category.api_name != ''

def test_get_content_by_category():
    fake_form: FormData = FormUseCase.convertJsonInFormData('fake_form.json')

    assert len(fake_form.categories) > 0

    category: Category = FormUseCase.getCategoryByPosition(fake_form.categories, 1)[0]

    assert category.position == 1
    assert category.api_name != ''    

    contents: list[Content] = FormUseCase.getContentByCategory(fake_form.contents, category.api_name)

    assert len(contents) > 0

   
