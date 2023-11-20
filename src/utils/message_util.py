from src.models.user_model import LevelAllow
class MessageUtil:
    def printIntro():
        intro_text = """
        Bem-vindo à jornada da cura secreta!
        
        Neste mundo da medicina e aprendizado, você embarcará em uma jornada emocionante. 
        Aqui, a curiosidade é sua maior aliada, e cada passo será uma oportunidade para expandir seu conhecimento.

        A medida que mergulha nessa jornada, descobrirá os segredos da medicina, evoluindo de novato para especialista.
        Suas ações moldarão seu caminho, e as responsabilidades crescerão à medida que seu conhecimento se aprofunda.

        Prepare-se para explorar, aprender e avançar. Sua busca pelo conhecimento começa agora! 
        """

        print(intro_text)

    def showLevels( levels_allowed: list[LevelAllow]): 
        if(len(levels_allowed) > 0):
            print('Breve apresentação dos niveis para percorrer nessa aventura da medicina!!')
            for level in levels_allowed:
                level_information = """
                    Titulo: {}
                    Legenda: {}
                    Level minimo: {}
                    level maximo: {}
            """.format(level['title'], level['text'], level['min_level'], level['max_level'])

                print(level_information)