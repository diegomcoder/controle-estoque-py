# TAKE AS IMPUT THE NUMBER OF SELECTABLE COMMANDS AND RETURN A NUMBER THAT REPRESENTS THE USER'S CHOICE
def get_user_command(param):
    options_numbers = []

    for i in range(param):
        options_numbers.append(f"{i +1}")
    
    while True:
        user_input = input('\nINSIRA O NÚMERO DO COMANDO DESEJADO AQUI 👉 ')

        if user_input in options_numbers:
            return int(user_input)
        else:
            print("🚫 COMMANDO INVÁLIDO!")