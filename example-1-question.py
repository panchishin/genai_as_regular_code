from llm_service import LLM
print("""

Let's use our LLM to answer questions with one word.
We will create a new LLM handler with the prompt "Answer questions with one word."
Then we can ask it questions easily, like a simple function call.

""")

# set up the handler
one_word_general_answers = LLM(prompt="Answer questions with one word.")

# ask a question
question = "What animal has no legs is sometimes called a danger noodle?"
print("Question:", question) 
print("Answer:", one_word_general_answers.process(data=question))

print("\n")
