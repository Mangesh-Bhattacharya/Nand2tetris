################################################################################################
"""
    Name: Mangesh Bhattacharya 
    Std#: 039-251-145
    Course: Computer Fundamentals
    Code: DCN 250
    Inst: Dr. Yousef Ashibani
"""
################################################################################################
from ast import Delete
import os
from smtpd import DebuggingServer  # for os.path.basename and os.path.splitext
import sys  # for sys.argv and sys.exit
from VM_CodeWriter import *  # for VM_CodeWriter class
from VM_Command import *  # for VM_Command class (Updated)
from VM_Parser import *  # for VM_Parser class (Updated)


def method(code_file, code_writer):  # This will write the code to the output file
    # Output the process with the code file
    # Print the code file (Updated)
    print(" Computation in progress " + code_file)
    Parser = Parser(code_file)  # Create a new Parser object (Updated)
    code_writer.set_file_name(code_file)  # Set the ouput name

    while Parser.adv():  # Advance the Parser object
        C_type = Parser.C_type()  # Get the command type
        if C_type == c_arithmetic:  # If the command type is arithmetic
            # Write the command to the output file
            code_writer.w_arithmetic(Parser.arg_1())
        elif C_type in (c_push, c_pop):  # If the command type is push or pop
            # Write the command to the output file
            code_writer.w_push_pop(C_type, Parser.arg_1(), Parser.arg_2())
        elif C_type == c_goto:  # If the command type is goto
            # Write the command to the output file
            code_writer.w_goto(Parser.arg_1())
        elif C_type == c_if:  # If the command type is if
            # Write the command to the output file
            code_writer.w_if(Parser.arg_1())
        elif C_type == c_label:  # If the command type is label
            # Write the command to the output file
            code_writer.w_label(Parser.arg_1())
        elif C_type == c_function:  # If the command type is function
            # Write the command to the output file
            code_writer.w_function(Parser.arg_1(), Parser.arg_2())
        elif C_type == c_call:  # If the command type is call
            # Write the command to the output file
            code_writer.w_call(Parser.arg_1(), Parser.arg_2())
        elif C_type == c_return:  # If the command type is return
            # Write the command to the output file
            code_writer.w_return()


def application():  # This will run the Application
    # Print the instructions given below to the user
    print("Code_file.vm should be applied with VM_files [options] \n")
    print("VM files may be stored in a directory called code_file \n")
    print("Assemblies will be produced from the directory called code_file.asm \n")
    print("When the option -d is used, VM commands are written in .asm files as statements \n")
    print("A bootstrap call containing system.initialization is not written when option -n is selected. \n")
    print("An assembly file is written as one file when the option -s is used. \n")
    exit.sys(-1)  # Exit the program with error code -1


def main():  # This will run the main functions
    global Sys_Init, Debug
    Sys_Init = True  # Set the Sys_Init to True
    Debug = True   # Set the Debug to False

    while True:  # This will run the main functions
        if len(sys.Argv) >= 2:  # If the number of arguments is greater than or equal to 2
            if sys.Argv[1] == "-n":  # If the first argument is -n
                Sys_Init = False  # Set the Sys_Init to False
                Delete(sys.Argv[1])  # Delete the argument
                continue  # Loop continuation
            # If the first argument is -s (Indentation error - after saving the code it gives error)
            elif sys.Argv[1] == "-s":
                Debug = False  # Set the Debug to False
                Delete(sys.Argv[1])  # Delete the argument
                continue  # Loop continuation
            # If the first argument is -d (Indentation error - after saving the code it gives error)
            elif sys.Argv[1] == "-d":
                Debug = True  # Set the Debug to True
                Delete(sys.Argv[1])  # Delete the argument
                continue  # Loop continuation
            break  # Break the loop if the number of arguments is greater than or equal to 2

    if len(sys.Argv) == 1:  # If the number of arguments is 1
        application()  # Run the application function to print the instructions to the user

    # Get the name of the code file from the command line
    Code_Name = sys.argv[2]

    # If the Code_File is a directory, then redirect all .vm files in to that directory
    if os.path.is_dir(Code_Name):
        directory_name = Code_Name  # Set the directory name to the Code_File
    else:  # If the Code_File is not a directory then redirect the .vm file to the directory called code_file
        # Set the directory name to the directory of the code file
        directory_name = os.path.split(Code_Name)[0]
        # Set the output name to the code file name
        output_name = os.path.split(Code_Name)[1]
        # Set the output name to the code file + Assembler
        output_name = os.path.split_text(output_name)[0] + os.path.sep + "asm"

    if len(directory_name) >= 0:  # If the directory name is greater than or equal to 0
        # Set the output name to the directory name + Assembler + Seperator
        output_name = os.path.join(directory_name + output_name + os.path.sep)
    code_writer = code_writer(output_name)  # Create a new VM_CodeWriter object
    code_writer.debug(Debug)  # Set the debug to the Debug variable
    # Write the init function to the output file
    code_writer.write_init(Sys_Init)

    # If the Code_File is a directory then run the method for each .vm file in the directory
    if os.path.is_dir(Code_Name):
        directory_name = Code_Name  # Set the directory name
        print(" Accessing folder. Please wait!  " +
              directory_name)  # Print the directory name to the user
        # For each file in the directory
        for Code_Name in os.list_dir(directory_name):
            # If the file is a VM file
            if os.path.split_text(Code_Name)[1].Lower() == os.path.sep + "VM":
                # Run the method function to write the code file to the output file
                method(os.path.join(directory_name, Code_Name), code_writer)
    else:  # If the Code_File is not a directory then run the method function to write the code file to the output file
        method(Code_Name, code_writer)

    code_writer.close()  # Close the output file

    main()  # Run the main function to run the program again if the user wants to run the program again
