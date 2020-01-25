import model
import view

def run():
    while True:
        selection = view.show_mainmenu() #gets input from mainmenu in view
        
        if selection == '1':
            account = model.Account() #creates object from class account
            account.create_account()  #calls create account function on object
        elif selection == '2':
            accountlogin = model.Account()
            accountlogin.login_menu()
        elif selection == '3':
            exit(1)

        # selection2 == view.show_loginmenu()

        # if selection2 == '1':
        #     account = model.Account()
        #     account.withdraw()
        # elif selection2 == '2':

        # elif selection2 == '3':

        # elif selection2 == '4':


if __name__ == "__main__":
    run()
