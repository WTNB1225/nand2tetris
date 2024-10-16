from parser import *
from symbol_table import Symbol_table
import code
import re
import argparse
import os

symbol_pattern = re.compile(r'([0-9]+)|([0-9a-zA-Z_\.\$:]+)')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('asm_file', type=str, help='asm file')
    args = parser.parse_args()
    asm_file = args.asm_file
    save_file = os.path.splitext(asm_file)[0] + '.hack'
    symbol_table = Symbol_table()
    with HackParser(asm_file) as hp:
        op_address = 0
        while hp.advance() != None:
            cmd_type = hp.command_type()
            if cmd_type == A_COMMAND or cmd_type == C_COMMAND:
                op_address+=1
            elif cmd_type == L_COMMAND:
                symbol_table.add_entry(hp.symbol(), op_address)
            
    with HackParser(asm_file) as hp:
        with open(save_file, 'w') as wf:
            while hp.advance() != None:
                cmd_type = hp.command_type()
                if cmd_type == A_COMMAND:
                    symbol = hp.symbol()
                    m = symbol_pattern.match(symbol)
                    if m.group(1): #@value
                        bincode = "0" + int2bin(int(m.group(1)), 15)
                    elif m.group(2): #@symbol
                        symbol = m.group(2)
                        if symbol_table.contains(symbol):
                            address = symbol_table.get_address(symbol)
                            bincode = "0" + int2bin(address, 15)
                        else:
                            symbol_table.add_variable(symbol)
                            address = symbol_table.get_address(symbol)
                            bincode = "0" + int2bin(address, 15)

                elif cmd_type == C_COMMAND:
                    bincode = '111' + code.comp(hp.comp()) + code.dest(hp.dest()) + code.jump(hp.jump())

                if cmd_type != L_COMMAND:
                    wf.write(bincode + '\n')




def int2bin(value, bitnum):
    bin_value = bin(value)[2:]
    if len(bin_value) > bitnum:
        raise Exception('Over binary size')
    return "0" * (bitnum - len(bin_value)) + bin_value

if __name__ == '__main__':
    main()