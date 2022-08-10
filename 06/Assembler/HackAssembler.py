#!/usr/bin/env/python3

################################################################################################
"""
    Name: Mangesh Bhattacharya 
    Course: Computer Fundamentals
    Code: DCN 250
    Inst: Dr. Yousef Ashibani
"""
################################################################################################

import asm, code, symtable, Parser # import from asm, symbol table, and parser 
from curses.ascii import isdigit  # Determines if the string is a digit

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
