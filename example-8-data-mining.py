from llm_service import LLM
import json

print("""
All the previous examples covered classification or correction tasks.
In this example we will extract data from a text.
Specifically we will extract the subject, verb, and object of a sentence.

We will use JSON to help the LLM produce easily parseable results.
""")


parse_subject = LLM(prompt="""Reply to my following message with the following json data:
{
    "subject": ... ,
    "verb": ... ,
    "object": ...
}""", format="json")


data_to_parse = (
    'According to the last messages from Stephanie, there is much needed attention on the braking system of the DRF',
    'On Tuesday, Jamie went to the store to buy some groceries',
    'Of all the people in London, only Greggory has never heard of the Queen',
    'UTTT is a game that is played on a 9x9 grid',
    'I am',
    'In the middle of the night, on a strange island, in a cabin made of honey, a bear woke up',
)


for sentence in data_to_parse:
    print("")
    print("Sentence :", sentence)
    result = json.loads(parse_subject.process(data=sentence))
    print("Subject :", result["subject"])
    print("Verb :", result["verb"])
    print("Object :", result["object"])


print("""
Done!
""")