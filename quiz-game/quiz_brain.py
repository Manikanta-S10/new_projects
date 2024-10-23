class Quiz_brain:
    def __init__(self,question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list
       

    def still_have_question(self):
        if len(self.question_list) <= self.question_number:
            print("Quiz completed")
            print(f"your final score is {self.score}/{len(self.question_list)}")
            return False 
        else:
            return True
            

    def next_question(self):
        current_question = self.question_list[self.question_number] 
        self.question_number += 1   
        user_answer = input(f"Q.{self.question_number}:{current_question.text}(True/False): ")
        self.check_answer(user_answer,current_question.answer)

   
    def check_answer(self,user_ans,correct_answer):
        if user_ans.lower() == correct_answer.lower():
            self.score += 1
            print('you got it right!')
            print(f'your score is {self.score}/{self.question_number}')
        else:
            print('you got it wrong')
            print(f'your score is {self.score}/{self.question_number}')
        print(f'right answer is: {correct_answer}') 
        


