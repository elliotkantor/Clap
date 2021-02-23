# clap.py - add clap emojis in between every word
import pyperclip
clap = "👏"
userSentence = input("-> ").split()
result = ""
for word in userSentence[:-1]:
    result += word + clap
result += userSentence[-1]
print(result)
pyperclip.copy(result)
print("Copied to clipboard")