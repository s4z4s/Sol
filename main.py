import json
import difflib
import random

def chatbot():
    with open("trainer.json", "r") as file:
        data = json.load(file)

    print("Hi, I'm Future. How can I help you today?")
    print("I can also code a little bit in python!")
    print("I learn from your answers, so if I do not know\nan answer, I will ask you to provide one!")

    memory = {}
    previous_question = None

    while True:
        user_input = input("\nYou: ")
        user_input = user_input.lower()
        words = user_input.split()

        if user_input in data:
            response = data[user_input]
            print(f"\nFuture: {response}")
            memory[user_input] = response
            previous_question = user_input
        elif any(word in data for word in words):
            for word in words:
                if word in data:
                    response = data[word]
                    print(f"\nFuture: {response}")
                    memory[word] = response
                    previous_question = word
                    break
        elif "why" in user_input or "how" in user_input:
            if previous_question:
                print(f"\nFuture: Can you please provide more context and clarify what you mean by 'why' or 'how' regarding the question '{previous_question}'?")
            else:
                print("\nFuture: I'm sorry, I don't have enough information to answer that question.")
        else:
            closest_question = difflib.get_close_matches(user_input, data.keys(), n=1, cutoff=0.6)
            if closest_question:
                closest_question = closest_question[0]
                response = data[closest_question]
                print(f"\nFuture: {response}")
                memory[user_input] = response
                previous_question = closest_question
            else:
                answer = input("\nFuture: I'm sorry, I don't understand. Can you provide an answer for that question? (y/n) ")
                if answer == "y":
                    new_answer = input("\nWhat is the answer? ")
                    data[user_input] = new_answer
                    with open("Data_Request.json", "a") as file:
                        file.write(json.dumps({user_input: new_answer}) + '\n')
                    print("\nThank you! I have learned a new answer.")
                else:
                        closest_question = difflib.get_close_matches(user_input, data.keys(), n=1, cutoff=0.6)
                        if closest_question:
                            closest_question = closest_question[0]
                            response = data[closest_question]
                            print(f"\nFuture: {response}")
                            memory[user_input] = response
                            previous_question = closest_question
                        elif "why" in user_input or "how" in user_input:
                            if previous_question:
                                print(f"\nFuture: Can you please provide more context and clarify what you mean by 'why' or 'how' regarding the question '{previous_question}'?")
                        else:
                                print("\nFuture: I'm sorry, I don't have enough information to answer that question.")
chatbot()
