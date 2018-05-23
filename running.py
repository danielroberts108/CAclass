import halp, quiz

class running:
    def __init__(self):
        while True:
            cmd=str(input("<+> "))
            if cmd == "X":
                exit()
            elif cmd == "?":
                halp()
            elif cmd=="quiz":
                quiz()