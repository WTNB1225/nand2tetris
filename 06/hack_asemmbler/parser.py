import re
A_COMMAND_PATTERN = re.compile(r'@([0-9a-zA-Z_\.\$:]+)')
L_COMMAND_PATTERN = re.compile(r'\(([0-9a-zA-Z_\.\$:]*)\)')
C_COMMAND_PATTERN = re.compile(r'(?:(A?M?D?)=)?([^;]+)(?:;(.+))?')

A_COMMAND = 0
L_COMMAND = 1
C_COMMAND = 2



class HackParser:
    def __init__(self, filepath):
        self.file = open(filepath)
        self.current_command = None
        
    def advance(self):
        while True:
            line = self.file.readline()
            if not line:
                self.current_command = None
                break
            line_trimmed = line.strip().replace(' ', '')
            comment_index = line_trimmed.find('//')
            if comment_index != -1:
                line_trimmed = line_trimmed[:comment_index]
            if line_trimmed != '':
                self.current_command = line_trimmed
                break
        return self.current_command
    
    def command_type(self):
        if self.current_command[0] == '@':
            return A_COMMAND
        elif self.current_command[0] == '(':
            return L_COMMAND
        else:
            return C_COMMAND
        
    def symbol(self):
        cmd_type = self.command_type()
        if cmd_type == A_COMMAND:
            m = A_COMMAND_PATTERN.match(self.current_command)
            if not m:
                raise Exception('Parsing symbol failed')
            return m.group(1)
        elif cmd_type == L_COMMAND:
            m = L_COMMAND_PATTERN.match(self.current_command)
            if not m:
                raise Exception('Parsing symbol failed')
            return m.group(1)
        else:
            raise Exception('Current command is not A_COMMAND or L_COMMAND')

    def dest(self):
        cmd_type = self.command_type()
        if cmd_type == C_COMMAND:
            m = C_COMMAND_PATTERN.match(self.current_command)
            return m.group(1)
        else:
            raise Exception('Cunrrent command is not C_COMMAND')

    def comp(self):
        cmd_type = self.command_type()
        if cmd_type == C_COMMAND:
            m = C_COMMAND_PATTERN.match(self.current_command)
            return m.group(2)
        else:
            raise Exception('Cunrrent command is not C_COMMAND')

    def jump(self):
        cmd_type = self.command_type()
        if cmd_type == C_COMMAND:
            m = C_COMMAND_PATTERN.match(self.current_command)
            return m.group(3)
        else:
            raise Exception('Cunrrent command is not C_COMMAND')



