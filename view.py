import model

def show_mainmenu():            #first user prompt

    print("Hello. Please choose an option:")
    print("1. Create an account")
    print("2. Login")
    print("3. Exit Terminal")

    option = input()
    while option not in ['1', '2', '3']:
        option = input("Sorry, invalid input. Try again.")
    return option


# def show_loginmenu():       #second user prompt

#     print("Welcome", #enter user first name and last name)
#     print("How may we help you today?")
#     print("1. Withdraw")
#     print("2. Deposit")
#     print("3. Check Balance")
    

#     option = input()
#     while option not in ['1', '2', '3']:
#         option = input("Sorry, invalid input. Try again.")
#     return option
