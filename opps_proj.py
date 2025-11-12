class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input('''Welcolme to Chatbook!! How would you like to proceed? 
                           1. Press 1 to signup
                           2. Press 2 to login
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit''')
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
    
    def signup(self):
        email = input("Enter your email id Here -> ")
        password = input("SetUp  your password Here -> ")
        self.username = email
        self.password = password
        print("Signup Successful!!")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username == '' and self.password == '':
            print("No user found, please signup first")
        else:
            usernm = input("Enter your email id Here -> ")
            passwd = input("Enter your password Here -> ")
            if usernm == self.username and passwd == self.password:
                print("You have successfully logged in")
                self.loggedin = True
            else:
                print("Invalid Credentials, please try again")
        print("\n")
        self.menu()
obj = chatbook()