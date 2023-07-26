# TAKE AS IMPUT THE NUMBER OF SELECTABLE COMMANDS AND RETURN A NUMBER THAT REPRESENTS THE USER'S CHOICE
def get_user_command(param):
    optionsNumbers = []

    for i in range(param):
        optionsNumbers.append(f"{i +1}")
    
    while True:
        userInput = input('\nINSIRA O NÚMERO DO COMANDO DESEJADO AQUI 👉 ')
        if userInput in optionsNumbers:
            return userInput