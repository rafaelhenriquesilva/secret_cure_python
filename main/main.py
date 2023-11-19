import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
print(f"Projeto root: {project_root}")

from src.utils.json_util import JSONUtil
from src.utils.message_util import MessageUtil
from src.useCases.user_use_case import UserUseCase
from src.models.user_model import UserInfo, UserData, LevelAllow

def execute():
    MessageUtil.print_intro()

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