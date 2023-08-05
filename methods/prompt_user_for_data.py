from modules import *

def prompt_user_for_data(regex, text=""):
    if regex:
        user_input = input(f"{text }")
        ok = re.search(regex, user_input)
        if ok != None:
            return user_input
        return prompt_user_for_data(regex, text)