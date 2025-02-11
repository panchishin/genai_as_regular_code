from llm_service import LLM

print("""
Not just spam or safe, let's classify items as ANIMAL, VEGETABLE, or MINERAL.
""")


def classify_item(item):
    # our handler
    item_classifier = LLM(prompt="Reply to my following message as either 'ANIMAL', 'VEGETABLE', 'MINERAL'.  The message is a description of an object.")

    # classify the item as ANIMAL, VEGETABLE, MINERAL or UNKNOWN
    response = item_classifier.process(data=item).upper()
    if response in ["ANIMAL", "VEGETABLE", "MINERAL"]:
        return response
    else:
        return "UNKNOWN"


things = [
    "a dog", 
    "three cats", 
    "a lovely paper box coloured with blue and white hearts", 
    "carrot sticks", 
    "rocks", 
    "a rock", 
    "Beyonce", 
    "The Rock"
    ]

for thing in things:
    classification = classify_item(thing)
    print(thing, "=", classification)


print("""
Notice it didn't do so well with "The Rock"
We will address that in the next example.
""")