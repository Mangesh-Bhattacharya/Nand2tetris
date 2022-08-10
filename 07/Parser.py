# Hack VM translator parser class
################################################################################################
"""
    Name: Mangesh Bhattacharya 
    Course: Computer Fundamentals
    Code: DCN 250
    Inst: Dr. Yousef Ashibani
"""
################################################################################################

from numpy import empty  # Import the empty function
from VMCommand import *  # Import the VMCommand class


class Parser(object):  # Create a new class

    # The code will initialize the class with the source file name.
    def __init__(Self, Source_Name):
        Self.File = open(Source_Name, "Read")  # The code will open the file
        Self.Line = "   "  # The code will set the value of Line to empty
        Self.Line_Number = 0  # The code will set the value of Line_Number to 0
        Self.Raw_Line = "   "  # The code will return the value of the command type

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
        # Code is a C-type that takes in a string arithmetic and returns the result of the string.
        if Self.C_Type in (arithmetic):
            # The code will call the parse_arg_1() method on Self.
            Self.parse_arg_1()
        # If the command is not push or pop, the code will call the parse_arg_2() method on Self.
        if Self.C_Type not in (push, pop):
            # The code will call the parse_arg_2() method on Self.
            Self.parse_arg_2()

    def parse_c_type(Self):  # First the commands will be run on Whitespace.
        Self.Line = Self.Line.lstrip()  # Removes Whitespaces
        # If it finds one, it stores the text before and after the found line break into variables named Command
        m = Self.Line.find("    ")
        # The code will find the first instance of " " in the line, and then remove it.
        if m != -1:
            # The code will also find the last instance of " " in the line, and then remove it.
            Com = Self.Line[:m]
            # The code will set the value of Line to the value of the line after the command.
            Self.Line = Self.Line[m:]
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

    def C_Type(Self):  # Will revert the Command Type
        """
            This code will revert the type of commands mentioned below: (Refered from slide 189 of Chpater 7)
                c_arithmetic = 1    # which involve the add, sub, neg, eq, lt, gt, and, or, and not
                c_pop = 2           # Pop and Push are the Memory Commands 
                c_push = 3         # which involve the push and pop commands
        """
        return Self.C_Type  # Will revert the Command Type

    def parse_arg(Self):  # Of non-whitespace, Argument is next to execute
        # This "lstrip" is used as a function because it produces a string replica only with leading characters deleted, i.e., "    push".
        # Only the whitespace and quotes will be removed
        Self.Line = Self.Line.lstrip()
        # When a substring is discovered in a provided string, this method returns the lowest index or first occurrence of the substring.
        m = Self.Line.find("    ")
        # If the m is not eaual to -1, if m != -1: The code checks to see if the line is not at the end of the file,
        # and then it assigns that line to a variable called Command.
        if m != -1:
            # The code will assign the value of Command to the variable Arg.
            Arg = Self.Line[:m]
            # The code will set the value of Line to the value of the line after the command.
            Self.Line = Self.Line[m:]
        else:  # The code will check if the user input is empty.
            # The code will print the value of Argument to the console.
            Arg = Self.Line
            Self.Line = "   "   # The code will set the value of Line to empty
        # The code attempts to return the argument passed in as string.
        if len(Arg) == 0:
            return Arg  # Will return the Argument
        else:  # The code will return the Argument
            # The code will return an empty string if the argument is not passed.
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
