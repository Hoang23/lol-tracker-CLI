from os import system, name 
from typing import List

class chatCLI:
    def __init__(self, top: int, jg: int, mid: int, bot: int, sup: int, notes: list, allcommands: list):
        self.top = top
        self.jg = jg
        self.mid = mid
        self.bot = bot
        self.sup = sup
        self.notes = notes
        self.allcommands = allcommands

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
        self.allcommands = []


    def sums(self):
        print("top: " + str(self.top))
        print("jg: " + str(self.jg))
        print("mid: " + str(self.mid))
        print("bot: " + str(self.bot))
        print("sup: " + str(self.sup))
        

    def createNote(self): 
        for note in self.notes:
            print(note)
            
    def info(self):
        chatCLI.sums(self)
        chatCLI.createNote(self)
      
    def main(self):
        print("Program has started")

        while True:
            print("\n")
            print("Enter input")
            _input = str(input())
            self.allcommands.append(_input)
            latestInput = _input.split()
            
            chatCLI.clear(self)
            
            if "top" in latestInput:
                for words in latestInput:
                    if words.isdigit():
                        self.top = int(words)
                        
            if "mid" in latestInput:
                for words in latestInput:
                    if words.isdigit():
                        self.mid = int(words)
                      
            if "jg" in latestInput:
                for words in latestInput:
                    if words.isdigit():
                        self.jg = int(words)
                       
            if "bot" in latestInput:
                for words in latestInput:
                    if words.isdigit():
                        self.bot = int(words)
                       
            if "sup" in latestInput:
                for words in latestInput:
                    if words.isdigit():
                        self.sup = int(words)
                        
            if "/note" in latestInput:
                self.notes.append(_input)
               
            if "/reset" in _input:
                chatCLI.reset(self)
            
            chatCLI.info(self)
                
            
            print("\n\n\n")
            
            print("All commands: ")
            for line in self.allcommands:
                print(line)