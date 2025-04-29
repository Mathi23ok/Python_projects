print(":::::::::::::::::Simple Quiz App::::::::::::::::::::::")

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["a) London", "b) Paris", "c) Rome", "d) Madrid"],
        "answer": "b"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["a) Earth", "b) Venus", "c) Mars", "d) Jupiter"],
        "answer": "c"
    },
    {
        "question": "Who wrote 'Harry Potter'?",
        "options": ["a) J.K. Rowling", "b) Stephen King", "c) Charles Dickens", "d) Mark Twain"],
        "answer": "a"
    }
]

score = 0
for q in questions:
    print("\n"+q["question"])
    for option in q["options"]:
        print(option)
        
    user_ans = input("Enter your answer(a/b/c/d): ").lower()

    if(user_ans == q["answer"]):
        print("Correct!")
        score += 1
    else:
        print(f"Wrong the correct answer was {q['answer']}")
print(f"\nFinal score : {score}/{len(questions)}")
print("Thank you ... come again")
