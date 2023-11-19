import json
import os

class JSONUtil:
    @staticmethod
    def loadJson(file):
        data = ''
        script_directory = os.path.dirname(os.path.abspath(__file__))  # Diretório do script
        file_path = os.path.join(script_directory, file)
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
