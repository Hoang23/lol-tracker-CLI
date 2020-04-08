from os import system, name 
from typing import List

class chatCLI:
    def __init__(self, top: int, jg: int, mid: int, bot: int, sup: int, notes: list):
        self.top = top
        self.jg = jg
        self.mid = mid
        self.bot = bot
        self.sup = sup
        self.notes = notes

    # define our clear function 
    def clear(self): 
      
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
      
        # for mac and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear') 

    def reset(self):
        self.top = 0
        self.jg = 0
        self.mid = 0
        self.bot = 0
        self.sup = 0
        self.notes = []


    def sums(self):
        print("top: " + str(self.top))
        print("jg: " + str(self.jg))
        print("mid: " + str(self.mid))
        print("bot: " + str(self.bot))
        print("sup: " + str(self.sup))
        

    def createNote(self): # takes in a list
        for note in self.notes:
            print(note)
            
    def info(self):
        chatCLI.sums(self)
        chatCLI.createNote(self)
      
    def main(self):
        print("Program has started")

        while True:
            print("Enter input")
            _input = str(input())
            latestInput = _input.split()
            
            chatCLI.clear(self)
            
            if "top" in latestInput:
                for words in latestInput:
                    if words.isdigit():
                        self.top = int(words)
                        chatCLI.info(self)
            elif "mid" in latestInput:
                for words in latestInput:
                    if words.isdigit():
                        self.mid = int(words)
                        chatCLI.info(self)
            elif "jg" in latestInput:
                for words in latestInput:
                    if words.isdigit():
                        self.jg = int(words)
                        chatCLI.info(self)
            elif "bot" in latestInput:
                for words in latestInput:
                    if words.isdigit():
                        self.bot = int(words)
                        chatCLI.info(self)
            elif "sup" in latestInput:
                for words in latestInput:
                    if words.isdigit():
                        self.sup = int(words)
                        chatCLI.info(self)
            elif "note" in latestInput:
                self.notes.append(_input)
                chatCLI.info(self)
            elif "reset" in _input:
                chatCLI.reset(self)
            else:
                chatCLI.info(self)
            
            print("\n\n\n")

CLI = chatCLI(0, 0, 0, 0, 0, [])
CLI.main()