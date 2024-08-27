# quiz_game.py

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    }
]

# def ask_question(question):
#     print(question["question"])
#     for idx, option in enumerate(question["options"], 1):
#         print(f"{idx}. {option}")
#     answer = input("Choose the correct option (1/2/3/4): ")
#     return question["options"][int(answer) - 1]

# def play_quiz():
#     score = 0
#     for question in questions:
#         answer = ask_question(question)
#         if answer == question["answer"]:
#             print("Correct!")
#             score += 1
#         else:
#             print(f"Incorrect! The correct answer was {question['answer']}.")
#         print()
#     print(f"Quiz finished! Your final score is {score}/{len(questions)}.")

# if __name__ == "__main__":
#     play_quiz()

def ask_question(question):
    print(question["question"])
    for idx,option in enumerate(question["options"],1):
        print(f"{idx}.{option}")
    answer = input("choose the correct option (1/2/3/4) : ")
    return question["options"][int(answer)-1]

def ask_quiz():
    score =0
    for question in questions :
        answer = ask_question(question)
        if answer == question["answer"]:
            print("correct !")

        else:
            print(f"incorrect! correct answer was {question['answer']}")
        print()
    print(f"quiz finished ! your final score is {score}/{len(questions)}")

if __name__ == "__main__" :
    ask_quiz()