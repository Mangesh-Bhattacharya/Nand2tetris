#!/usr/bin/python

import sys  # Import the sys module
import os  # Import the os module
from CodeWriter import *  # Import the code writer class
from Parser import *  # Loop through all the files in the directory
from VMCommand import *  # Loop through all the files in the directory


def method(code_file, code_writer):  # This will write the code to the output file
    # Output the process with the code file
    print(" Computation in progress " + code_file)  # Print the code file
    Parser = Parser(code_file)  # Create a new Parser object
    code_writer.set_file_name(code_file)  # Set the file name

    while Parser.advance():  # Advance the Parser object
        C_type = Parser.C_type()  # Get the command type
        if C_type == c_arithmetic:  # If the command type is arithmetic
            # Write the command to the output file
            code_writer.w_arithmetic(Parser.arg_1())
        elif C_type in (c_push, c_pop):  # If the command type is push or pop
            # Write the command to the output file
            code_writer.w_push_pop(C_type, Parser.Arg_1(), Parser.Arg_2())


def main():  # This will run the program
    # If the length is not equal to 3, then print the following message.
    if len(sys.argv) != 3:
        # Print the following message
        print(" Use the VM Code_file.vm to view ")
        # Print the following message
        print(" If the Code_File is a directory then all VM regualted files ")
        # Print the following message
        print(" must be applied to that particular Code_File")
        return  # Return from the function

    Code_Name = sys.argv[2]  # Get the name of the code file

    # If the Code_File is a directory, then redirect all .vm files in to that directory
    if os.path.is_dir(Code_Name):
        directory_name = Code_Name  # Set the directory name
        print(" Accessing folder. Please wait!  " +
              directory_name)  # Print the directory name
        # Set the output name
        output_name = os.path.split(Code_Name)[2] == os.sep.path + "VM"
        output_name = directory_name + os.path.sep + output_name  # Set the output name
        # Create a new code writer object
        code_writer = code_writer(output_name)
        # Loop through all the files in the directory
        for Code_Name in os.list_dir(directory_name):
            # If the file is a .vm file
            if Code_Name.endswith(".vm"):
                # Set the code file name
                code_file = directory_name + os.path.sep + Code_Name  # Set the code file name
                method(os.path.ext_sep + directory_name +
                       code_file, code_writer)  # Call the method
    else:  # If the Code_File is a file
        # Create a new code writer object
        code_writer = code_writer(Code_Name)  # Set the code file name
        output_name = os.path.split(
            Code_Name)[1] + ".asm"  # Set the output name
        # Call the method
        method(Code_Name, code_writer)

    code_writer.close()  # Close the output file


main()  # Call the main function
