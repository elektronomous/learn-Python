from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def main():
    question_bank = [Question(Q["question"], Q["correct_Trueanswer"]) for Q in question_data];
    quiz_brain = QuizBrain(question_bank);

    """
    The longest way:

    question_bank = []

    for data in question_data:
        question_bank.append(Question(data["text"], data["answer"]))

    """

    while quiz_brain.still_has_question():
        quiz_brain.next_question();

    print("You've completed the quiz.");
    print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}");
    

if __name__ == "__main__":
    main();