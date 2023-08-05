from modules import *
import json
with open('./data/msg.json', encoding="utf-8") as my_json:
    msg = json.load(my_json)

lang = "pt"
msg = msg[lang]

# EXIT PROGRAM
def exit_program():
    os.system("cls")
    print(msg["bye"])
    quit()