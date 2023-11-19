import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
print(f"Projeto root: {project_root}")

from src.utils.json_util import JSONUtil
from src.utils.message_util import MessageUtil
from src.useCases.user_use_case import UserUseCase
from src.models.user_model import UserInfo, UserData, LevelAllow

JSON_USER_NAME = 'user_infos.json'

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