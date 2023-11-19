class LevelAllow:
    def __init__(self, name, level, email, text):
        self.name = name
        self.level = level
        self.email = email
        self.text = text

    def __getitem__(self, key):
        if key == 'level':
            return self.level
        elif key == 'email':
            return self.email
        elif key == 'name':
            return self.name
        elif key == 'text':
            return self.text
        else:
            raise KeyError(f"Chave inválida: {key}")
        

class UserInfo: 
    def __init__(self, name, level, email):
        self.name = name
        self.level = level
        self.email = email

    def __getitem__(self, key):
        if key == 'level':
            return self.level
        elif key == 'email':
            return self.email
        elif key == 'name':
            return self.name
        else:
            raise KeyError(f"Chave inválida: {key}")
        
class UserData:
    def __init__(self, levels_allowed, user_info):
        self.levels_allowed = levels_allowed
        self.user_info = user_info

    def __getitem__(self, key):
        if key == 'user_info':
            return self.user_info
        elif key == 'levels_allowed':
            return self.levels_allowed
        elif key == 'text':
            return self.text
        else:
            raise KeyError(f"Chave inválida: {key}")       