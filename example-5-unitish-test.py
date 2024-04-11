from llm_service import LLM

print("""
Previously we classified items as ANIMAL, VEGETABLE, or MINERAL but we didn't do so well with "The Rock".
Let's try to improve our classifier by tweaking the directive.
This is the art of 'Prompt Engineering'.
We are going to approach this in a unit-testish way.

In a business setting, you would likely have some examples of scenarios where the classifier failed, 
customer feedback, or some other data to guide you.

As you change your directive (which is what we are calling our prompt) you will want 
to make sure it continues to work on the previous test cases and any new failure cases you find.

Using a unit-testish approach can help you make sure you are improving your model and not breaking it.

We will start with the previous directive then try variations.  Press enter to continue after each test.
""")

class Classifier:
    def __init__(self, directive):
        self.llm = LLM(directive=directive)

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


def score_directive(directive):
    correct = 0
    total = 0
    classifier = Classifier(directive)
    for thing, classification in things_and_classification.items():
        prediction = classifier.classify_item(thing)
        total += 1
        if prediction == classification:
            correct += 1
        else:
            print(thing, "=", classification, "!=", prediction)

    return correct / total


directive = "Reply to my following message as either 'ANIMAL', 'VEGETABLE', 'MINERAL'.  The message is a description of an object."
print("\nDefault directive:", directive)
print("Score for default directive:", score_directive(directive))

x = input("Press enter to continue...")

directive = "Reply to my following message as either 'ANIMAL', 'VEGETABLE', 'MINERAL'.  Pay attention to famous movie stars.  The message is a description of an object."
print("\nAlternate directive:", directive)
print("Score for custom directive:", score_directive(directive))

x = input("Press enter to continue...")

directive = "Reply to my following message as either 'ANIMAL', 'VEGETABLE', 'MINERAL'.  The message is a description of an object or the name of a person."
print("\nAlternate directive:", directive)
print("Score for custom directive:", score_directive(directive))

x = input("Press enter to continue...")

directive = "Reply to my following message as either 'ANIMAL', 'VEGETABLE', 'MINERAL'.  Music, movie, and wrestling stars are ANIMALS."
print("\nAlternate directive:", directive)
print("Score for custom directive:", score_directive(directive))

print("""
Done!
""")