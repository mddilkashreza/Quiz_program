quiz = {
    "question1":{
        "question": "What is capital of France?",
        "answer": "Paris"
    },

    "question2":{
        "question": "What is capital of Germany?",
        "answer": "Berlin"
    },

    "question3":{
        "question": "What is capital of Italy?",
        "answer": "Rome"
    },
    "question4":{
        "question": "What is capital of Nepal?",
        "answer": "Kathmandu"
    },
    "question5":{
        "question": "What is capital of India?",
        "answer": "New Delhi"
    },
    "question6":{
        "question": "What is capital of USA?",
        "answer": "Washington D.C"
    },
    "question7":{
        "question": "What is capital of Bangladesh?",
        "answer": "Dhaka"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer ?")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score +1
        print("Your score is :"+str(score))
    else:
        print("Wrong")
        print("The answer is :" + value['answer'])
        print("Your score is :"+str(score))