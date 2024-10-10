class CodeWriter:
    def __init__(self, filepath):
        self.file = open(filepath)

    def __enter__(self):
        return
    
    def __exit__(self, type, value, traceback):
        return
    
    def set_file_name(self, file_name):
        print("start converting to " + file_name)

    def write_arithmetic(self, command):

        return
    
    def write_push_pop(self, command, segment, index):
        return
    
    def close(self):
        self.file.close()