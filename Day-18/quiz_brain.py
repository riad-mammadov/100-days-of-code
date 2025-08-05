class Quiz:
    def __init__(self,list):
        self.number = 0
        self.list = list
        self.score = 0
    
    def next_question(self):
        current = self.list[self.number]
        self.number += 1
        user_answer = input(f"Q.{self.number}: {current.text} (True/False): ")
        self.check_ans(user_answer, current.answer)

    def still_active(self):
        return self.number < len(self.list)
    
    def check_ans(self,user,correct):
        if user.lower() == correct.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
            print(f"The correct answer was {correct}")
        
