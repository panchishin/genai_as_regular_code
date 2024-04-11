from llm_service import LLM
import json

print("""
Lastly, we can do a lot more than just classification.
In this example we will do some error handling,
specifically fixing syntax errors in json data.
""")

fix_json = LLM(directive="Fix the syntax errors in the following json data", format="json")

data_to_parse = (
    '{"name": "John", "age": 30, "city": "New York"}',
    '{"name": "Peter", "age": 45, "city": "Paris"}',
    '{"name": "Kate", "age: 25, "city": "London"}',
    '{name: Tyler, age = \'79, city: London}',
)

for data in data_to_parse:
    print("")
    try:
        result = json.loads(data)
        print("VALID ✅", data)
    except:
        print("ERROR ❌", data)

        fixed_data = fix_json.process(data=data)
        result = json.loads(fixed_data)
        print("FIXED ✅", json.dumps(result))


print("""
Done!
""")