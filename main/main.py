import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from src.utils.json_util import JSONUtil
from src.utils.message_util import MessageUtil
from src.useCases.user_use_case import UserUseCase
from src.models.user_model import UserInfo, UserData
from src.useCases.form_use_case import FormUseCase
from src.models.form_model import FormData, Category

JSON_USER_NAME = 'user_infos.json'
JSON_FORM_NAME = 'form.json'
TEXT_JSONS = {
     "PUT_CATEGORY_TEXT": "Escolha um categoria pelo numero: ",
     "CONTINUE_TO_QUESTIONS": "Deseja fazer os testes para evoluir no estudo sobre a medicina? (s/n): ",
     "STUDY_MORE": "Continue engajado(a) em seus estudos e realize o teste quando se sentir confiante"
}

def execute():
    try:
            # Ações do cliente
            MessageUtil.printIntro()
            data_user_json: UserData = JSONUtil.loadJson(JSON_USER_NAME)
            user_info: UserInfo = UserUseCase.captureUserInfoData()
            data_to_update: UserData = UserUseCase.updateUserInfo(user_info, data_user_json) 
            print(UserUseCase.createMessageUserInfo(user_info))
            JSONUtil.createJson(data_to_update, JSON_USER_NAME)

            # Ações do game
            MessageUtil.showLevels(data_user_json['levels_allowed'])
            execute_game()
    except Exception as e:
            print("Erro na execução do programa", e)
    
def execute_game():
    data_form_json: FormData = FormUseCase.convertJsonInFormData(JSON_FORM_NAME)
    FormUseCase.showCategories(data_form_json.categories)

    categoryOption = int(input(TEXT_JSONS['PUT_CATEGORY_TEXT']))
    categories: list[Category] = FormUseCase.getCategoryByPosition(data_form_json.categories, categoryOption)
    
    if(categories and len(categories) > 0):
            contents = FormUseCase.getContentByCategory(data_form_json.contents, categories[0].api_name)

            if(len(contents) > 0):
                        FormUseCase.showContents(contents, categories[0].title) 

                        doQuestions = input(TEXT_JSONS['CONTINUE_TO_QUESTIONS'])
                        if doQuestions.lower() != 's':
                            print(TEXT_JSONS['STUDY_MORE']) 
                        else:
                            print('questions')

            else:
                print('Não foi encontrado a conteudo para esta categoria.')      
    else:
        print('Não foi encontrado a categoria.') 
    
def main():
    while True:
        try:
            execute()
            repetir = input("Deseja executar o programa novamente? (s/n): ")
            if repetir.lower() != 's':
                print("Encerrando o programa.")
                break
        except Exception as e:
            print("Erro durante a execução:", e)

if __name__ == "__main__":
    main()