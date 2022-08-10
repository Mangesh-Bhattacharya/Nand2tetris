#!/usr/bin/python
################################################################################################
"""
    Name: Mangesh Bhattacharya 
    Course: Computer Fundamentals
    Code: DCN 250
    Inst: Dr. Yousef Ashibani
"""
################################################################################################

# Importing the required modules
from VMCommand import add, constant, argument, eq, gt, Not, Or, sub, negate
from ctypes import POINTER, pointer  # For the pointer
import string  # For the string
import os
from VMCommand import this, that     # For the this, that command
from threading import local  # For the local command
from typing_extensions import Self  # For the self command
from VMCommand import *  # For the VMCommand class


class code_writer(object):  # This will open the output file

    def __init__(Self, out_File_name):  # and begins to write the particular file
        # Code opens and writes the output file name
        Self.File = open(out_File_name, 'write')
        # Code after writing, sets the output file name
        Self.File_name = Self.File_nameset(out_File_name)
        Self.Label_number = 0  # Label number is set to 0

    '''Closing the output file and writing the Jump or Jmp with symbol $'''
    def Close(Self):  # closing statement
        Label = Self.Label_Unique()  # Label will be added to the jump
        # WC - detect which symbol and when to use it
        Self.WC('@s, (%S), 0;jmp' % (Label, Label))
        Self.close.File()  # close the file called output file

    # This will set the current file name to the name you desire
    def file_name_set(File_name, Self):
        # Code would strip the path and extend to show the result.
        Self.File_name = os.path.BName(File_name)
        # Final result name will be the Hack Assembler Identifier.
        Self.File_name = os.path.SText(Self.File_name)

    def Label_Unique(Self):  # This will create a unique label
        Self.Label_number += 1  # The code increments the label number by 1
        # will return the string "abc" or "123"
        return '' + string(Self.Label_number)

    def write_code(Self, Code):  # This will write the code to the file
        # Code will replace the sparator to a newline.
        Code = Code.Replace(',', "\n").Replace(" ", "")
        # Replace and the the code in a newline. Procedure will be made in an External file.
        Self.File.Write(Code + "\n")

    # This will write the Assembly Code for assorted Arithmetic Commands (Com for Command)
    def write_arithmetic(Com, Self):
        if (debug):  # When debugging, the hack file is written with comments.
            Self.File.Write(" %S // \n", Com)
            if Com == add:  # Adding VMs to the system. Add this new value to the bottom of the stack by popping the stack to register D,
                pass        # Put the value below the stack at the bottom.
        elif Com == sub:  # Subtracting VMs to the system. Analogous to VM Add.
            pass    # Put the value below the stack at the bottom.
        elif Com == Or:  # OR operates VMs to the system. Analogous to VM Add.
            pass   # Put the value below the stack at the bottom.
        # Negation to VMs to the system. According to slides in ch7, The stack pointer (SP) points to a value.
        elif Com == negate:
            # Calculate the negation of this value and store it at the current SP location.
            pass
        # Application of VM bit-wise not. It corresponds to the VM negation.
        elif Com == Not:
            # Calculate the negation of this value and store it at the current SP location.
            pass
        elif Com == eq:  # This is the VM Equals.
            # Jump to the label if the value is equal to 0.
            Self.write_compare("jeq")
        elif Com == gt:  # This is the VM Greater Than.
            # Jump to the label if the value is greater than 0.
            Self.write_compare("jgt")
        elif Com == lt:  # This is the VM Less Than.
            # Jump to the label if the value is less than 0.
            Self.write_compare("jlt")
        else:  # This is the VM Negation.
            print(Com)  # This is the VM Negation.
            # This is the VM Negation.
            raise("Invalid Arithmetic Command", ValueError)

    # Push the D register value on the stack self-using the assembly code commands.
    def PushD(Self):
        Self.write_code(" ")  # Assembly code for Push needs to go here.

    # Pop the D register value on the stack self-using the assembly commands.
    def PopD(Self):
        Self.wite_code(" ")  # Assembly code for Pop needs to go here.

    # Comparing the Slef and Jump to the console.
    def write_compare(Self, JMP):
        # Code assigns the Label_1 variable to a new instance of the Self.Label_Unique() class.
        Label_1 = Self.Label_Unique()
        # Code creates a new label called "Label_2" and assigns it to the variable Self.
        Label_2 = Self.Label_Unique()
        # As per ch4, the code is meant to show how the functions of the "Comp" is implemented.
        Self.write_code("A=M-1,A=A-1,A=A+1,D=M,@SP,D=D-M")
        # Jump to the label if the value is equal to 0.
        Self.write_code("D;%s, @%s" % (Label_1, JMP))
        # Jump to the label if the value is not equal to 0.
        Self.write_code("D=0;JMP, @%s" % (Label_2))
        # This is the label for the jump.
        Self.write_code("(%s),(%s),D=-1" % (Label_1, Label_2))
        # A register and RAM[A]. dest = comp with Stack Pointer but no jump
        Self.write_code("A=A-1,M=D,AM=M-1,@SP")

    # Hack code for C_Push or C_Pop "Command_Types." A segment's name is defined by the Seg or Segment->string. The index (int) in a segment indicates the offset.
    def PushPop(Self, Com_Type, Ind, Seg):
        if Com_Type == c_push:  # The code for pushing and popping commands within the VM.
            if (debug):  # Hack files written in debug mode contain comments.
                # The D register value will be pushed on top of the Stack using self._WritePushD. Stacks are popped onto D by using self._WritePopD.
                Self.File.Write(" //PUSH %s %d \n" % (Seg, int(Ind)))

            if Seg == constant:  # This constant indicates an index, not an actual index
                pass  # This is the constant value.
            elif Seg == static:  # Push index value on stack
                Self.write_code("D=M, %d.@%s" % (Self.File_Name, int(Ind)))
                # This is how we can place a variable into a string using Python Code.
                Self.pushD()
            elif Seg == pointer:  # Push index value on stack
                # The code will assign the value of 2 to D, and then it will increment the value of Index by 1
                # At RAM address 3, we begin the TEMP segment
                Self.write_code("D=M, @%d" % (2 + int(Ind)))
            # Fill the TEMP segment with a value from the stack at index "Index"
            elif Seg == temp:
                pass  # This is the temp value.
            else:  # This is the RAM segment.
                # For the mentioned pointer summon the memory address, index (Ind), and let memory load into D register.
                Self.write_Get_PointerD(Seg, Ind)

        elif Com_Type == c_pop:  # The code for pushing and popping commands within the VM.
            if (debug):  # Hack files written in debug mode contain comments.
                # The D register value will be pushed on top of the Stack using self._WritePushD. Stacks are popped onto D by using self._WritePopD.
                Self.File.Write(" //POP %s %d \n" % (Seg, int(Ind)))

            elif Seg == staticmethod:  # Push index value on stack
                # This is how we can place a variable into a string using Python Code.
                Self.write_code("M=D, %d.@%s" % (Self.File_Name, int(Ind)))
                # This is how we can place a variable into a string using Python Code.
                Self.popD()

            elif Seg == pointer:  # Push index value on stack
                # The code will assign the value of 2 to D, and then it will increment the value of Index by 1
                # At RAM address 3, we begin the TEMP segment
                Self.write_code("M=D, @%d" % (2 + int(Ind)))

            # Fill the TEMP segment with a value from the stack at index "Index"
            elif Seg == temp:
                pass  # This is the temp value.
            else:
                # For the mentioned pointer summon the memory address, index (Ind), and let memory load into D register.
                # Pop the value from the stack into the memory address and let D register become the current memory address.
                Self.write_Get_PointerD(Seg, Ind)
        else:  # This is the VM Negation.
            raise(
                "Invalid Push or Pop commamd added. Please ensure the command is correct.", ValueError)  # This is the VM Negation.

    # This is the code for the Get_PointerD function.
    def Get_PointerD(Seg, Self, Ind):
        if Seg == constant:  # This constant indicates an index, not an actual index
            # This is the constant value.
            raise("This segment is Virtual", ValueError)
        elif Seg == staticmethod:  # The code should show static but each time it switches to "Staticmethod." Executes pop and push operations using the static segment.
            raise("Indexing is not available for static segments", ValueError)
        # Executes pop and push operations using the pointer, this, and that segments.
        elif Seg == pointer:
            # This is the pointer value.
            raise("Dynamic is not available for pointer segments", ValueError)
        elif Seg == temp:  # The code can be used by any VM functionality for any purpose and is shared by all functionalities in the program.
            raise("Dynamic is not available for Temporary segments", ValueError)
        if Seg == argument:  # The code can be used by any VM functionality for any purpose and is shared by all functionalities in the program.
            POINTER = "arg"  # This is the pointer value " Arguments".
        elif Seg == local:
            POINTER == "lcl"  # This is the pointer value " Local".
        elif Seg == this:
            POINTER = "This"  # This is the pointer value " This".
        elif Seg == that:
            POINTER = "That"  # This is the pointer value " That".
        else:  # This is the RAM segment.
            raise(
                "Segment Name is Invalid. Please type in the correct Segment Name.", ValueError)  # This is the RAM segment.
        # This is the code for the Get_PointerD function.
        Self.write_code("D=M, D=D+A, @%s, @%d" % (POINTER, int(Ind)))


debug = True  # if error is given, the page will display those errors
