from llm_service import LLM

print("""
Previously we classified items as ANIMAL, VEGETABLE, or MINERAL but we didn't do so well with "The Rock".

In a business setting, you would likely have some examples of scenarios where the classifier failed, 
customer feedback, or some other data to guide you.

As you try to improve your prompt you will want to make sure it continues to work on the previous test
cases and any new failure cases you find.

Using a unit-testish approach can help you make sure you are improving your model and not breaking it.

We will start with the previous prompt then try variations.  Press enter to continue after each test.
""")

class Classifier:
    def __init__(self, prompt):
        self.llm = LLM(prompt=prompt)

    def classify_item(self, item):
        response = self.llm.process(data=item)
        if response in ["ANIMAL", "VEGETABLE", "MINERAL"]:
            return response
        else:
            return "UNKNOWN"


things_and_classification = {
    "a dog" : "ANIMAL",
    "three cats" : "ANIMAL",
    "a lovely paper box coloured with blue and white hearts" : "VEGETABLE",
    "carrot sticks" : "VEGETABLE",
    "rocks" : "MINERAL",
    "a rock" : "MINERAL",
    "Beyonce" : "ANIMAL",
    "'The Rock'" : "ANIMAL",
}


def score_prompt(prompt):
    correct = 0
    total = 0
    classifier = Classifier(prompt)
    for thing, classification in things_and_classification.items():
        prediction = classifier.classify_item(thing).upper()
        total += 1
        if prediction == classification:
            correct += 1
        else:
            print(thing, "=", classification, "!=", prediction)

    return correct / total


prompt = "Reply to my following message as either 'ANIMAL', 'VEGETABLE', 'MINERAL'.  The message is a description of an object."
print("\nDefault prompt:", prompt)
print("Score for default prompt:", score_prompt(prompt))

x = input("Press enter to continue...")

prompt = "Reply to my following message as either 'ANIMAL', 'VEGETABLE', 'MINERAL'.  Pay attention to famous movie stars.  The message is a description of an object."
print("\nAlternate prompt:", prompt)
print("Score for custom prompt:", score_prompt(prompt))

x = input("Press enter to continue...")

prompt = "Reply to my following message as either 'ANIMAL', 'VEGETABLE', 'MINERAL'.  The message is a description of an object or the name of a person."
print("\nAlternate prompt:", prompt)
print("Score for custom prompt:", score_prompt(prompt))

x = input("Press enter to continue...")

prompt = "Reply to my following message as either 'ANIMAL', 'VEGETABLE', 'MINERAL'.  Music, movie, and wrestling stars are ANIMALS."
print("\nAlternate prompt:", prompt)
print("Score for custom prompt:", score_prompt(prompt))

print("""
Done!
""")