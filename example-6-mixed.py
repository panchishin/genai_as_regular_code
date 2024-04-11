from llm_service import LLM
print(""""
Let's improve our spam classifier's speed.

We may have some hard business rules that don't need a LLM to process,
so we can use them to quickly classify some emails as SPAM or SAFE.

If it doesn't match any of those rules, we can use the LLM to classify it.

This leverages the speed of classic code and the flexibility of LLM!
""")

def fast_spam_classifier(email, user_name):
    if user_name.lower() in email.lower():
        return "SAFE"
    
    known_spam_phrases = ["bahamas", "click here", "free trip", "egyptian prince"]
    for phrase in known_spam_phrases:
        if phrase.lower() in email.lower():
            return "SPAM"

    return "UNKNOWN"

slow_spam_classifier = LLM(directive="Reply to my following message as either SPAM or SAFE.  The message is an email text.").process

def spam_classifier(email, user_name):
    result = fast_spam_classifier(email, user_name)
    return result if result != "UNKNOWN" else slow_spam_classifier(data=email)


email_messages = (
    "Dear Contest Winner!  You have won a free trip to the Bahamas.  Please provide your bank account information to claim your prize.",
    "Hey Derik, I hope you are doing well.  I wanted to let you know that I am going to be late to the meeting today.  I will be there as soon as I can.  Thanks!  -John",
    "Click here to claim your prize!",
    "Hot singles in your neighbourhood are waiting for you! http://hot.singles.com",
    "Jane, Derik, and Sylvia, please be advised that tomorrow we are hosting the annual company picnic.  Please bring a dish to share but not pasta salad. Noone likes that stuff -Molly",
)

for email in email_messages:
    print("\nEmail text:", email)
    print("Response:", spam_classifier(email, user_name="Derik"))

print("""
Now that was MUCH FASTER than just using the LLM for everything!
""")
