class details:
    def __init__(self):
        self.fn = ""
        self.sn = ""
        self.age = ""

    def get(self):
        self.fn = input("What's your forename? ")
        self.sn = input("Whats your surname? ")
        self.age = input("How old are you? ")
        self.un = (self.fn[0:3] + self.sn[0:3] + self.age)

    def save(self):
        self.fn = input("Please enter your first name: ")
        self.ln = input("Please enter your surname: ")
        while True:
            try:
                self.age = int(input("Please enter your age: "))
            except ValueError:
                print("Input not valid, please re-enter age.")
                continue
            else:
                break
        self.un = self.fn[0:3] + self.ln[0:3] + self.age
        print("Username is: " + self.un)
        while True:
            self.pw = input("Enter password: ")
            self.pw2 = input("Enter password again: ")
            if self.pw == self.pw2:
                break
            else:
                print("Passwords do not match. Please try again.")
                continue
        self.file = open("students.txt", "a")
        self.file.write(self.un)
        self.file.write(self.pw)
        self.file.close()
        det = (self.fn + "\n" + self.ln + "\n" + str(self.age))
        self.file.open(self.un + ".txt", "w")
        self.file.write(det)
        self.file.close()