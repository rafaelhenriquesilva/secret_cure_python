from src.models.user_model import UserInfo, UserData

class UserUseCase:
    def updateUserInfo(user_info: UserInfo, dataToUpdate: UserData):
        dataToUpdate['user_info']['name'] = user_info.name
        dataToUpdate['user_info']['email'] = user_info.email
        dataToUpdate['user_info']['level'] = user_info.level

        return dataToUpdate
    
    def createMessageUserInfo(user_info: UserInfo):
        message_user_info = f"""
            Jogador: {user_info.name},
            Email: {user_info.email},
            level: {user_info.level}
        """

        return message_user_info