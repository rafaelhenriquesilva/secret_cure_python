from src.models.user_model import UserInfo, UserData, LevelAllow
from src.models.form_model import Question

class UserUseCase:
    def updateUserInfo(user_info: UserInfo, dataToUpdate: UserData):
        try:
            dataToUpdate['user_info']['name'] = user_info.name
            dataToUpdate['user_info']['email'] = user_info.email
            dataToUpdate['user_info']['level'] = user_info.level

            return dataToUpdate
        except Exception as e:
            print("Erro ao atualizar os dados dos usuários", e)
        
    
    def captureUserInfoData(name='', email=''): 
        try:
            if name=='' and email == '':
                name = input('Por favor, informe seu nome: ')
                email = input('Por favor, informe seu email: ')

            level = 0

            user_info = UserInfo(name, level, email)

            return user_info
        except Exception as e:
            print("Erro ao coletar os dados dos usuários", e)


    
    def createMessageUserInfo(user_info: UserInfo, levels_allowed: list[LevelAllow]):
        try:
            print('\n Parabéns pela atuação \n')
            message_user_info = f"""
                    Jogador: {user_info.name},
                    Email: {user_info.email},
                    level: {user_info.level}

            """
            print(message_user_info)
            print('\n Sua etapa na jornada: \n')
            for levelAllow in levels_allowed:
                if(user_info['level'] >= levelAllow['min_level'] and user_info['level'] <= levelAllow['max_level']):
                    level_information = """
                        Titulo: {}
                        Legenda: {}
                    """.format(levelAllow['title'], levelAllow['text'])
                    print(level_information)

            return message_user_info
        except Exception as e:
            print("Erro ao montar a messagem com dados do usuário", e)

    def updateLevelUser(user_info: UserInfo, correct_questions: list[Question]):
        try:
            for question in correct_questions:
                if(user_info.level <= 100):
                    user_info.level += 1
            
            return user_info
        except Exception as e:
            print("Erro ao montar a messagem com dados do usuário", e)
        
    


