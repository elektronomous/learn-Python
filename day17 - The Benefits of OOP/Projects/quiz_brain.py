class QuizBrain:
    
    def __init__(self, q_list:list):
        self.question_list = q_list;
        self.question_number = 0;
        self.score = 0;
    
    def still_has_question(self):
        return self.question_number < len(self.question_list);
  
           
    def next_question(self):
        question = self.question_list[self.question_number];
        self.question_number += 1;
        # ask the user to input their answer
        answer = input(f"Q.{self.question_number}: {question.text}(True/False): ");
        # then check the answer
        self.check_answer(answer, question.answer);
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!");
            self.score += 1;
        else:
            print("That's wrong");
        
        print(f"The correct answer is {correct_answer}.");
        print(f"The current score is: {self.score}/{self.question_number}.\n");