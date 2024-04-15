from llm_service import LLM
import json

print("""
All the previous examples covered classification or correction tasks.
In this example we will extract data from a text.
Specifically we will extract the subject of a sentence.

In this example we use a 2 examples in our prompt to help the LLM understand the task.
""")

parse_subject = LLM(prompt="""Reply to my following message with just the subject of the sentence.
For example, if my message is 'When Billy went to the store he remembered to buy cheese' then your reply will be 'Billy'.
For example, if my message is 'LLMs are a great data mining tool' then your reply will be 'LLMs'.
Only use the information in my following message to determine the subject.""")

data_to_parse = (
    'According to the last messages from Stephanie, there is much needed attention on the braking system of the DRF',
    'On Tuesday, Jamie went to the store to buy some groceries',
    'Of all the people in London, only Greggory has never heard of the Queen',
    'UTTT is a game that is played on a 9x9 grid',
)

for sentence in data_to_parse:
    print("")
    print("Sentence :", sentence)
    print("Subject :", parse_subject.process(data=sentence))

print("""
Done!
""")