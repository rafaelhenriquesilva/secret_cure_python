import sys
import os

# Obtendo o caminho absoluto do diretório atual (__tests__) e adicionando o diretório pai (SecretCure) ao PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.useCases.user_use_case import UserUseCase
from src.models.user_model import UserInfo

def test_create_message_user_info():
    message_user_info = ''
    user_info = UserInfo('Test', 'test@mail.com', 1)
    message_user_info = UserUseCase.createMessageUserInfo(user_info)
    assert message_user_info != ''
    assert message_user_info == f"""
            Jogador: {user_info.name},
            Email: {user_info.email},
            level: {user_info.level}
        """

    
