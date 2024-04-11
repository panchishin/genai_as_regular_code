from llm_service import LLM
print("""

Let's use our LLM to classify email messages as SPAM or SAFE.
Again, the setup is super easy.  We create a new LLM handler with a simple English directive.
Then we can use it to classify email messages as SPAM or SAFE.
""")

spam_classifier = LLM(directive="Reply to my following message as either SPAM or SAFE.  The message is an email text.")

email = "Dear Contest Winner!  You have won a free trip to the Bahamas.  Please provide your bank account information to claim your prize."
print("\nEmail text:", email)
print("Response:", spam_classifier.process(data=email))

email = "Hey Derik, I hope you are doing well.  I wanted to let you know that I am going to be late to the meeting today.  I will be there as soon as I can.  Thanks!  -John"
print("\nEmail text:", email)
print("Response:", spam_classifier.process(data=email))

print("""
Done!
""")
