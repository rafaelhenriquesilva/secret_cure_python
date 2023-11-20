from src.models.form_model import Question, Answer
from src.models.response_model import ResponseForm
import random

class QuestionUseCase:
    
    def getQuestionsByCategory(questions: list[Question], category: str):
          filtered_question = [question for question in questions if question['category'] == category]
          return filtered_question
    
    def showQuestionsAndAwnsers(questions: list[Question], category: str):
        filtered_question = QuestionUseCase.getQuestionsByCategory(questions, category)
        questionCorrects = []
        for question in filtered_question:
            print('\n----- {} -----\n'.format(question.text))

            questionCorrects = QuestionUseCase.shuffledAnswersAndShow(question.answers, question, questionCorrects)

           
            
        print('Você acertou a quantidade: {}'.format(len(questionCorrects)))
        responseForm = ResponseForm(questionCorrects, filtered_question)
        return responseForm            

    def shuffledAnswersAndShow(answers: list[Answer], question: Question, questionCorrects: list[Question]):
        
        shuffled_answers = []
        vowels = ['a', 'b', 'c']
        if len(answers) > 0:
                shuffled_answers = random.sample(answers, len(answers))
                for idx, answer in enumerate(shuffled_answers):
                    answer.set_vowel(vowels[idx])
                    print('\n  {} - {}  \n'.format(answer.vowel, answer['text']))
                    
                isCorrect = QuestionUseCase.answeringQuestionAndReturnResult(shuffled_answers, question.correct_answer_id)

                if(isCorrect == True):
                     questionCorrects.append(question)

        return questionCorrects         
                     
    def answeringQuestionAndReturnResult(shuffled_answers: list[Answer], correct_answer_id):
        try:
            user_vowel_answer = input("Qual opção você acha que esta correta? \n")
            user_vowel_answer = str.lower(user_vowel_answer)
            
            filtered_answer = [answer for answer in shuffled_answers if answer['vowel'] == user_vowel_answer]

            if (filtered_answer[0].answer_id == correct_answer_id):
                print('\n Resposta correta \n')
                return True
            else:
                print('\n Resposta incorreta \n')
                return False  
        except Exception as e:
            print("Erro ao escolher a resposta", e)
       

