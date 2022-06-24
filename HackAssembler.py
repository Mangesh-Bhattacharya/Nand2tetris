#!/usr/bin/env/python3

import code, symtable, Parser # import from asm, symbol table, parser, and system
from venv import main  # import from virtual environment
from curses.ascii import isdigit  # Determines if the string is a digit

# Dictionary for reference 
"""
    comp = {
        "0": "0101010",
        "1": "0111111",
        "-1": "0111010",
        "D": "0001100",
        "A": "0110000",
        "!D": "0001111",
        "!A": "0110000",
        "-D": "0001111",
        "-A": "0110011",
        "D+1": "0011111",
        "A+1": "0110111",
        "D-1": "0001110",
        "A-1": "0110010",
        "D+A": "0000010",
        "D-A": "0010011",
        "A-D": "0000111",
        "D&A": "0000000",
        "D|A": "0010101",
        "M": "1110000",
        "!M": "1110001",
        "-M": "1110011",
        "M+1": "1110111",
        "M-1": "1110010",
        "D+M": "1000010",
        "D-M": "1010011",
        "M-D": "1000111",
        "D&M": "1000000",
        "D|M": "1010101"
    }

    # Destination with binary
    dest = {
        "null": "000",
        "M": "001",
        "D": "010",
        "A": "100",
        "MD": "011",
        "AM": "101",
        "AD": "110",
        "AMD": "111"
    }

    # Jump with binary JLE, JEQ, JGT, JGE, JLT, JNE, JMP
    jump = {
        "null": "000",
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111"
    }

    # In assembly, the symbol table is populated with standard notes
    tables = {
        "SP": "0",
        "LCL": "1",
        "ARG": "2",
        "THIS": "3",
        "THAT": "4",
        "SCREEN": "16384",
        "KBD": "24576",
    } 
"""
class assembler:
    # To understand Seneca College's code, we have to make the code or the program read the Add.asm or Max.asm source file. 
    # Therefore, it can create a new file called Add.hack or Max.hack, which later gets transformed into an assembled code as a text file.

    def __init__(self):
        self.address_symbol = 16  # address starts for symbolic variables.
        self.table_symbol = symtable.symtable()

    # Let us suggest a file name for our hack code program or source file.
    def hack_file(asm):
        if asm.endswith(".asm"):  # I have added a parameter called asm
            # which is a program file communicated in Hack assembly lang.
            return asm.replace("asm", ".hack")
        else:
            return asm + ".hack"  # This recovers the string as mentioned
    
    def addr_get(self, symbol):
        if isdigit.symbol():  # This is a helper method
            return symbol
        else:
            # Observes the symbols address by detecting if it has decimal, variable or label
            if not self.contains.table_symbol(symbol):
                # value by decimal, variable or label
                self.add_entry.table_symbol(self.address_symbol, symbol)
                # A final value is assigned to a variable by adding the two values.
                self.address_symbol += 1
                # Address will be returned.
                return self.table_symbol.get_addr(symbol)
    
    def first_pass(File, self): # First compilation pass is helping to 
        # calculate the location of the label definition in memory
        parser = Parser.Parser(File)
        addr_curr = 0 # current address is 0 or Zero
        while parser.more_inst():  # Parameter check
            parser.adv() # Advanced parser
            instruction_type = instruction_type.parser # the two different instruction types
            # C-Instruction - Therefore if it starts with @ then type must change to A because if it is not a comment and blank line then it must show Type C
            if instruction_type in [parser.instA, parser.instC]:
                # A final value is assigned to a variable by adding the two values.
                addr_curr += 1
            elif instruction_type == parser.instL:  # This code represent the Label definition part
                # This program attempts to add an entry to the symbol table
                self.table_symbol.add_entry(symtable.Symbol.parser, addr_curr)
    
    # Second compilation pass helping to write results to an output file using the hack machine code.
    def sec_pass(asm, self, hack):
        # Parameter output to write the hack machine language.
        with open(hack, "write") as hack:
            code = code.Code() # refering to asm program
            # Convert data into rquired Hack format.
            parser = Parser.Parser(asm)
            while parser.more_inst():  # This line is for getting the result of the Second Pass.
                parser.adv()
                # Generate hack language for both Add and Max asm files in Second Pass
                instruction_type = instruction_type.parser
                if instruction_type == parser.instA: # if identified as instruction-A then 
                    # wirte the address with the specific symbol as a newline
                    hack.write(code.gen_instA(
                        self.addr_get(parser.symbol)) + '\n')
                elif instruction_type == parser.instC:
                    # If identified as instruction-A then wirte the address with the specific dest = comp ; jmp as a newline.
                    hack.write(code.gen_instC(
                        self.addr_get(parser.destination, parser.compute, parser.jump)) + '\n') 
                elif instruction_type == parser.instL: 
                    pass
    
    # This is the primary method. Ensures the production process is carried out.
    def Assemble(self, File):
        # First Pass parameter - the Hack Assembly Language code file contains the source code for a program.
        self.first_pass(File)
        # Second Pass parameter - the Hack Assembly Language code file contains the source code for a program.
        self.sec_pass(File, self.get_hack(File)) 

if __name__ == "__main__":
    # Once the code is compiled then you will recieved the mention message
    print("HackAssembler.py will now convert to Code.asm")

hack = assembler() 
hack.Assemble(asm)  # Transform ASM file to hack assembler file