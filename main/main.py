import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
print(f"Projeto root: {project_root}")

from src.utils.json_util import JSONUtil
from src.utils.message_util import MessageUtil
from src.useCases.user_use_case import UserUseCase
from src.models.user_model import UserInfo, UserData
from src.useCases.form_use_case import FormUseCase
from src.models.form_model import FormData, Category

JSON_USER_NAME = 'user_infos.json'
JSON_FORM_NAME = 'form.json'
def execute_game():
    data_form_json: FormData = FormUseCase.convertJsonInFormData(JSON_FORM_NAME)
    FormUseCase.showCategories(data_form_json.categories)

    categoryOption = int(input("Escolha um categoria pelo numero: "))
    categories: list[Category] = FormUseCase.getCategoryByPosition(data_form_json.categories, categoryOption)
    
    if(categories and len(categories) > 0):
        contents = FormUseCase.getContentByCategory(data_form_json.contents, categories[0].api_name)

        if(len(contents) > 0):
             FormUseCase.showContents(contents, categories[0].title) 
    else:
        print('Não foi encontrado a categoria.') 
    
   
      


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
    


def main():
    while True:
        try:
            execute()
            repetir = input("Deseja fazer outro pedido? (s/n): ")
            if repetir.lower() != 's':
                print("Encerrando o programa.")
                break
        except Exception as e:
            print("Erro durante a execução:", e)

if __name__ == "__main__":
    main()