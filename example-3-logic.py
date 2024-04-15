import shutil
from llm_service import LLM
import os

print("""
Building on the last spam detector,
Read email messages from files in the inbox folder
If a message is spam, move it to the spam folder otherwise move it to the safe folder
""")

spam_classifier = LLM(prompt="Reply to my following message as either SPAM or SAFE.  The message is an email text.")

for file in os.listdir("email/inbox"):
    with open("email/inbox/" + file, "r") as f:
        email = f.read()
        response = spam_classifier.process(data=email)
        if response == "SPAM":
            print("Moving email to SPAM folder email/spam/ :", file)
            shutil.move("email/inbox/" + file, "email/spam/" + file)
        elif response == "SAFE":
            print("Moving email to safe folder email/safe/ :", file)
            shutil.move("email/inbox/" + file, "email/safe/" + file)
        else :
            print("Unknown response:", response, "for email:", file)


print()
input("Press enter to move the emails back to the email/inbox folder...")

for file in os.listdir("email/spam"):
    shutil.move("email/spam/" + file, "email/inbox/" + file)
for file in os.listdir("email/safe"):
    shutil.move("email/safe/" + file, "email/inbox/" + file)

print("""
Done!
""")
