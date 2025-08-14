import google.generativeai as genai

# # pip install google.generativeai
import time

genai.configure(api_key= "")

model = genai.GenerativeModel("gemini-2.5-pro")
def myAi():
    while True:
        user_question=  input("Ask a question (or type 'quit' to exit): ")

        if user_question.lower() == 'quit':
            break

        response = model.generate_content(user_question)
        print(response.text)
        time.sleep(1)

    # # # wait for one second before sending the next response

myAi()
