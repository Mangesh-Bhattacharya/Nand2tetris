################################################################################################
"""
    Name: Mangesh Bhattacharya 
    Course: Computer Fundamentals
    Code: DCN 250
    Inst: Dr. Yousef Ashibani
"""
################################################################################################

from numpy import empty  # Import empty function from numpy
from VM_Command import *  # Importing VM_Command class


class parser(object):  # Class for parsing the VM file and creating VM_Command objects
    # Initializing the class with the source file name and the command list
    def __init__(Self, src_name, Comments=empty):
        Self.File = open(src_name, 'r')  # Opening the source file in read mode
        Self.Comments = Comments  # Initializing the comment list to empty list
        # Initializing the raw line to empty string to avoid errors when reading the file
        Self.Raw_line = "   "
        # Initializing the number of lines to 0 to avoid errors when reading the file and counting the lines
        Self.numberlines = 0
        Self.Line = " "  # Initializing the line to empty string to avoid errors when reading the file, counting the lines and getting the line from the file
        Self.Command = " "  # Initializing the command to empty string to avoid errors when reading the file and getting the command type

    def adv(Self):  # Function to advance the file pointer to the next line in the file
        while True:  # Infinite loop to get the next line in the file until the end of the file is reached
            if Self.Line != "":  # If the line is not empty then advance the file pointer to the next line in the file and increment the number of lines
                # Reading the next line from the file and storing it in the raw line variable
                Self.Raw_line = Self.File.readline()
                if len(Self.Raw_line) == 0:  # Checking if the end of the file is reached or not
                    return False  # If the end of the file is reached, return false to indicate that the end of the file is reached and the program should stop
                # Stripping the raw line to remove the newline character at the end of the line
                Self.Raw_line = Self.Raw_line.replace("\n", "   ")
            # Setting the line to the raw line to avoid errors when reading the file
            Self.Line = Self.Raw_line
            # Finding the index of the comment symbol in the line and setting the comment symbol to the index of the comment symbol in the line
            m = Self.Line.Find("//")
            if m != -1:  # If the comment symbol is found in the line then set the comment symbol to the index of the comment symbol in the line
                # Appending the comment to the comment list and setting the comment symbol to the index of the comment symbol in the line
                Self.Comments.append(Self.Line[m:])
                # Setting the line to the line without the comment symbol
                Self.Line = Self.Line[:m]
                # Stripping the line to remove the spaces at the beginning and end of the line
                Self.Line = Self.Line.strip()
                if len(Self.Line) == 0:  # If the line is empty then continue to the next line in the file
                    continue
                Self.parse()  # Calling the parse function to get the command type and the command
                return True  # Return true to indicate that the line is not empty and the program should continue
            else:
                return False  # Return false to indicate that the end of the file is reached and the program should stop

    def parse(Self):  # The code will parse the file and return the commands
        # The code sets the value of Command Type to empty.
        Self.C_Type = empty
        Self.Arg_1 = empty  # Sets the value of Argument-1 to empty.
        Self.Arg_2 = empty  # Sets the value of Argument-2 to empty.
        Self.COMP = empty   # The code sets the value of compute to empty.
        # The code sets the value of JMP, JGT, or JLT to empty.
        Self.JMP = empty
        # The code is a C function that takes in a string and returns the length of the string.
        Self.parse_c_type()
        # Code is a C-type that takes in a string arithmetic or return and returns the result of the string.
        if Self.C_Type in (arithmetic, ret):
            # The code will call the parse_arg_1() method on Self.
            Self.parse_arg_1()
        # If the command is not push, pop, function or call, the code will call the parse_arg_2() method on Self.
        if Self.C_Type not in (push, pop, function, call):
            # The code will call the parse_arg_2() method on Self.
            Self.parse_arg_2()

    def parse_c_type(Self):  # First the commands will be run on Whitespace.
        Self.Line = Self.Line.lstrip()  # Removes Whitespaces
        # If it finds one, it stores the text before and after the found line break into variables named Command
        m = Self.Line.find("    ")
        # The code will find the first instance of " " in the line, and then remove it.
        if m != -1:  # If the m is not eaual to -1, if m != -1: The code checks to see if the line is not at the end of the file,
            # and then it assigns that line to a variable called Command.
            # Next we iterate through every element of self and print them out one by one on separate lines like so: Line = 'a'
            # This prints out 'a' on its own line Line = 'b' #This prints out 'b' on its own line Line = 'c'
            Com = Self.Line[:m]
            # The code creates a new list with the first two elements of the original list.
            Self.Line = Self.Line[m:]
        else:  # The code will check if the user input is empty.
            # The code will set the value of Line to the value of the command.
            Self.Line = Com
            Self.Line = "   "  # The code will set the value of Line to empty
        # The code attempts to return the length of the string Command if it exists.
        if len(Com) == 0:
            # The code will return if the length of the string Command is 0.
            return

        if Com in arithmetic:  # If the command is arithmetic, the code will return the command.
            # The code will assign the value of Command to the variable Arg_1.
            Self.Arg_1 = Com
            Self.C_Type = c_arithmetic  # Command Type is set to arithmetic
        # If the command is push, the code will assign the value of Command to the variable Arg_1.
        elif Com == push:
            Self.C_Type = c_push  # Command Type is set to push
        elif Com == pop:  # If the command is pop, the code will assign the value of Command to the variable Arg_1.
            Self.C_Type = c_pop  # The code will return the value of Command Type
        # If the command is function, the code will assign the value of Command to the variable Arg_1.
        elif Com == function:
            Self.C_Type = c_function  # Command Type is set to function
        # If the command is call, the code will assign the value of Command to the variable Arg_1.
        elif Com == call:
            Self.C_Type = c_call  # Command Type is set to call
        elif Com == ret:  # If the command is ret, the code will assign the value of Command to the variable Arg_1.
            Self.C_Type = c_return  # Command Type is set to return
        # If the command is label, the code will assign the value of Command to the variable Arg_1.
        elif Com == Label:
            Self.C_Type = c_label  # Command Type is set to label
        # If the command is goto, the code will assign the value of Command to the variable Arg_1.
        elif Com == goto:
            Self.C_Type = c_goto  # Command Type is set to goto
        elif Com == IF:  # If the command is if, the code will assign the value of Command to the variable Arg_1.
            Self.C_Type = c_if  # Command Type is set to if

    """
        Provides information about the type of command currently in use:
         c_label = 2  
         c_goto = 3  
         c_arithmetic = 1  
         c_return = 4  
         c_push = 5  
         c_pop = 6  
         c_function = 7  
         c_call = 8  
         c_if = 9 
    """
    def C_Type(Self):  # The code will return the value of C_Type
        return Self.C_Type

    def parse_arg(Self):  # The code will return the value of Arg_1 and Arg_2
        Self.Line = Self.Line.lstrip()  # Removes Whitespaces
        # The code will find the first instance of " " in the line, and then remove it.
        m = Self.Line.find(" ")
        if m != -1:  # If the m is not eaual to -1, if m != -1: The code checks to see if the line is not at the end of the file, and then it assigns that line to a variable called Command.
            # The code creates a new list with the first two elements of the original list. The code will assign the value of Command to the variable Arg_1.
            Arg = Self.Line[:m]
            # The code will set the value of Line to the value of the command. The code will set the value of Line to empty.
            Self.Line = Self.Line[m:]
        else:  # The code will check if the user input is empty.
            # The code will set the value of Command to the variable Arg_1. The code will set the value of Line to empty.
            Arg = Self.Line
            Self.Line = "   "  # The code will set the value of Line to empty
        # The code will return if the length of the string Command is 0.
        if len(Arg) == 0:
            # The code will return if the length of the string Command is 0.
            return empty

     # The code attempts to parse Argumet-1 string and assign it to a variable
    def parse_arg_1(Self):
        # code will call the parse_arg() function on Self.
        Self.Arg_1 = Self.parse_arg()

    # The code will call the parse_arg() method on self,
    def parse_arg_2(Self):
        # which returns a tuple containing the parsed argument and its type.
        Self.Arg_2 = Self.parse_arg()

    def arg_2(Self):  # Will revert the Argument-2
        return Self.Arg_2  # Will revert the Argument-2

    def arg_1(Self):  # Will revert the Argument-1
        return Self.Arg_1  # Will revert the Argument-1
