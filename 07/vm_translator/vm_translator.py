#!/usr/bin/python
# -*- coding: utf-8 -*-

from constant import *
from parser import Parser
from code_writer import CodeWriter
import glob
import argparse
import os.path


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('path', type=str, help='vm file or folder')

    args = parser.parse_args()
    path = args.path

    if path.endswith(".vm"):    # file
        with CodeWriter(path[:-3] + ".asm") as code_writer:
            translate_file(path, code_writer)
        print("Translated to", path[:-3] + ".asm")
    else:                       # directory
        if path.endswith("/"):
            path = path[:-1]
        with CodeWriter(path + ".asm") as code_writer:
            files = glob.glob("%s/*" % path)
            for file in files:
                if file.endswith(".vm"):
                    translate_file(file, code_writer)
        print("Translated to", path + ".asm")


#!/usr/bin/python
# -*- coding: utf-8 -*-

from constant import *
from parser import Parser
from code_writer import CodeWriter
import glob
import argparse
import os.path


def main():
    parser = argparse.ArgumentParser(description='Process VM files or folders.')
    parser.add_argument('path', type=str, help='VM file or folder')

    args = parser.parse_args()
    path = args.path

    if path.endswith(".vm"):    # If it's a file
        with CodeWriter(path[:-3] + ".asm") as code_writer:
            translate_file(path, code_writer)
        print(f"Translated to {path[:-3]}.asm")
    else:                       # If it's a directory
        if path.endswith("/"):
            path = path[:-1]
        with CodeWriter(path + ".asm") as code_writer:
            files = glob.glob(f"{path}/*.vm")
            for file in files:
                translate_file(file, code_writer)
        print(f"Translated to {path}.asm")


def translate_file(file, code_writer):
    filename, _ = os.path.splitext(os.path.basename(file))
    code_writer.set_current_translated_file_name(filename)
    with Parser(file) as ps:
        while ps.advance != None:
            ps.advance()
            if ps.current_command is None:
                continue
            if ps.command_type() == C_ARITHMETIC:
                code_writer.write_arithmetic(ps.arg1())
            elif ps.command_type() == C_PUSH:
                code_writer.write_push_pop(C_PUSH, ps.arg1(), ps.arg2())
            elif ps.command_type() == C_POP:
                code_writer.write_push_pop(C_POP, ps.arg1(), ps.arg2())
main()