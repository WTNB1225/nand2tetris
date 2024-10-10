C_ARITHMETIC = 0
C_PUSH = 1
C_POP = 2
C_LABEL = 3
C_GOTO = 4
C_IF = 5
C_FUNCTION = 6
C_RETURN = 7
C_CALL = 8

class Parser:
    def __init__(self, filepath):
        self.file = open(filepath, 'r')
        self.lines = self.file.readlines()
        for count, line in enumerate(self.lines):
            pass
        self.lines_index = 0
        self.lines_length = count
        self.current_command = None
    
    def __enter__(self):
        return
    
    def __exit__(self, type, value, traceback):
        return
    
    def has_more_commands(self):
        if self.lines_index > self.lines_length:
            return False
        else:
            return True
    
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
        if self.has_more_command == True:
            self.lines_index += 1
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
    
    def arg2(self):
        cmd_type = self.command_type()
        if cmd_type in [C_PUSH, C_POP, C_FUNCTION, C_CALL]:
            return self.current_command[2]
