import json
import os

class JSONUtil:

    # Função para a leitura de arquivos json
    @staticmethod
    def loadJson(file):
        try:
            data = ''
            script_directory = os.path.dirname(os.path.abspath(__file__)) 
            jsons_directory = os.path.join(script_directory, 'jsons') 

            file_path = os.path.join(jsons_directory, file)
            
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    data = json.load(file)
            else:
                print(f"Arquivo '{file}' não encontrado na pasta 'jsons'")
            return data
        except Exception as e:
            print("Erro ao carregar o json: {}".format(file), e)

    
    # Função para a escrita de arquivos json
    @staticmethod
    def createJson(data, json_name):
        try:
            script_directory = os.path.dirname(os.path.abspath(__file__))
            
            jsons_directory = os.path.join(script_directory, 'jsons')
            if not os.path.exists(jsons_directory):
                os.makedirs(jsons_directory)

            file_path = os.path.join(jsons_directory, json_name)
            with open(file_path, "w") as arquivo:
                json.dump(data, arquivo)
        except Exception as e:
            print("Erro ao criar o json: {}".format(json_name), e)

       