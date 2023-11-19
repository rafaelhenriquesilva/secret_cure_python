from src.models.user_model import UserInfo, UserData

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


    
    def createMessageUserInfo(user_info: UserInfo):
        try:
            message_user_info = f"""
                    Jogador: {user_info.name},
                    Email: {user_info.email},
                    level: {user_info.level}
            """

            return message_user_info
        except Exception as e:
            print("Erro ao montar a messagem com dados do usuário", e)
        
    


