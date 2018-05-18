import signup


class login:
    def __init__(self):
        self.un = input("Please enter your username or press [ENTER] if you don't have one: ")
        if self.un in open("students.txt").read():
            self.pw = input("Password: ")
            self.check = str(self.un + self.pw)
            if self.check in open("students.txt").read():
                self.file = open(self.un + ".txt", "r")
                self.data = self.file.read()
                self.file.close()
                self.data = self.data.split("\n")
                self.fn = self.data[0]
                self.sn = self.data[1]
                self.age = self.data[2]
                self.sco = self.data[3]
                self.det = (self.fn + "\n" + self.sn + "\n" + self.sco)
                print("Welcome back, " + self.fn)
            else:
                self.kg = 0
                while self.kg != 1:
                    print("Data not recognised. Try again?")
                    self.kg = int(input("YES = 0    NO = 1  :"))
                    if self.kg == 0:
                        login()
                    else:
                        print("Ok, bye.")
                        exit()
        elif self.un == "":
            signup()
        else:
            print("Username not recognised.")
            print("Would you like to register or try again?")
            self.ans = int(input("Register=0    Try=1   Neither=2"))
            if self.ans == 0:
                signup()
            elif self.ans == 1:
                login()
            else:
                exit()