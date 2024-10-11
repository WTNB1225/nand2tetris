from constant import *
class Parser:
    def __init__(self, filepath):
        self.file = open(filepath, 'r')
        self.current_command = None
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        self.file.close()
    
    def command_type(self):
        if self.current_command[0] == "push":
            return C_PUSH
        elif self.current_command[0] == "pop":
            return C_POP
        elif self.current_command[0] == "label":
            return C_LABEL
        elif self.current_command[0] == "goto":
            return C_GOTO
        elif self.current_command[0] == "if-goto":
            return C_IF
        elif self.current_command[0] == "function":
            return C_FUNCTION
        elif self.current_command[0] == "return":
            return C_RETURN
        elif self.current_command[0] == "call":
            return C_CALL
        elif self.current_command[0] in ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']:
            return C_ARITHMETIC
    
    def advance(self):
        while True:
            line = self.file.readline()
            if not line:
                self.current_command = None
                return self.current_command
            
            line = line.lstrip().rstrip()
            comment_index = line.find("//")
            if comment_index != -1:
                line = line[:comment_index]
            
            if line != "":
                self.current_command = line.split()
                return self.current_command
            
    def arg1(self):
        cmd_type = self.command_type()
        if cmd_type == C_ARITHMETIC:
            return self.current_command[0]
        else: 
            return self.current_command[1]
    
    def arg2(self):
        cmd_type = self.command_type()
        if cmd_type in [C_PUSH, C_POP, C_FUNCTION, C_CALL]:
            return self.current_command[2]