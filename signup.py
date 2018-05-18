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
        