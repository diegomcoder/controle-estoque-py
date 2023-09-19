# app.py: This is the main entry point of your application. It could set up the database and handle the main loop of your application, asking for user input and responding to it.

from views.textview import *
from views.category_view import print_stock_status

def get_user_command(regex):
    import re
    return re.search(regex, input())

def main():
    print_stock_status()

    opt = get_user_command('^[1-3]$')
    print(opt)

#implement_db()
main()