"""
    Name: Mangesh Bhattacharya 
    Std#: 039-251-145
    Course: Computer Fundamentals
    Code: DCN 250
    Inst: Dr. Yousef Ashibani
"""

import os  # for os.path.basename and os.path.dirname functions
from re import T  # Import the regular expression module for the 'T' token in the regex
import debugpy  # Import debugpy module (T = True) for debugging purposes
from numpy import empty  # for os.path.basename and os.path.dirname functions
from VM_Command import *  # for VM_Command class and its methods
from tkinter import FALSE  # Import FALSE from tkinter module for boolean values


class code_writer(object):  # Class code_writer inherits from object class

    def __init__(Self, out_file_name):  # out_name is the output file name
        Self.File = open(out_file_name, "write")  # open the output file
        Self.File_nameset(out_file_name)  # set the output file name

        Self.label = 0  # label counter
        Self.ret = empty  # return counter
        Self.call = empty  # call counter
        Self.halt_flag = FALSE  # if the program has halt

    def close(Self):  # close the output file
        if Self.halt_flag:  # if the program has halt
            if debugpy:  # if the debug is on
                Self.File.write("// <STOP>\n")
            Label = Self.Label_Unique()  # get the unique label
            # WC - detect which symbol and when to use it
            Self.WC('@s, (%S), 0;jmp' % (Label, Label))
        Self.close.File()  # close the file called output file

    def debugpy(Self, Value):  # print the debug message
        # if the debug in Python (py) is on, then debugpy = TRUE
        global debugpy
        debugpy = Value  # set the debug value

    # This will set the current file name to the name you desire
    def file_name_set(File_name, Self):
        # Code would strip the path and extend to show the result.
        Self.File_name = os.path.BName(File_name)
        # Final result name will be the Hack Assembler Identifier.
        Self.File_name = os.path.SText(Self.File_name)[1]
        if (debugpy):  # if the debug is on print the debug message
            Self.File.write("//     File_Name -  %s\n   " %
                            (Self.File_name))  # print the debug message and the file name
            Self.function_name = empty  # set the function name to empty string

    def write_initial(Self, Sys_initial=T):  # write the init command to the output file
        # if the program has halt then set the halt flag to TRUE
        Self.halt_flag = not Sys_initial
        if (debugpy):  # if the debug is on print the debug message
            # print the debug message and the file name
            Self.File.write(" // <Code Begins>  \n")
        # set the stack pointer to 256 (the top of the stack)
        Self.File.write("@256   \n D=A  \n    @SP   \n      M=D     \n")
        if (Sys_initial):  # if the program has halt then set the halt flag to TRUE
            Self.write_code(
                "M=-1,A=A+1,M=-1,A=A+1,M=-1,A=A+1,M=-1,A=A+1,M=-1,A=A+1,M=-1")  # write the initialization command to the output file
            # write the initialization command to the output file
            Self.write_call("Sys.initial", "0")
            Halt = Self.Label_Unique()  # get the unique label for the halt command
            # write the halt command to the output file
            Self.write_code("(%s),@%s,0;jmp" % (Halt, Halt))
            Self.halt_flag = T  # if the program has halt then set the halt flag to TRUE

    # Hack code for C_Push or C_Pop "Command_Types." A segment's name is defined by the Seg or Segment->string. The index (int) in a segment indicates the offset.
    def PushPop(Self, Com_Type, Ind, Seg):
        if Com_Type == c_push:  # The code for pushing and popping commands within the VM.
            if (debugpy):  # Hack files written in debug mode contain comments.
                # The D register value will be pushed on top of the Stack using self._WritePushD. Stacks are popped onto D by using self._WritePopD.
                Self.File.Write(" //PUSH %s %d \n" % (Seg, int(Ind)))
            if Seg == constant:  # This constant indicates an index, not an actual index
                Self.write_push_value(Ind)  # write the push value
            elif Seg == static:  # Push index value on stack
                # push the static memory
                Self.write_push_memory(Self.static(Ind))
            elif Seg == pointer:  # Push index value on stack
                # The code will assign the value of 2 to D, and then it will increment the value of Index by 1
                # At RAM address 3, we begin the TEMP segment
                Self.write_push_memory(2 + int(Ind))
            elif Seg == temp:  # Push index value on stack
                # The code will assign the value of 3 to D, and then it will increment the value of Index by 1
                Self.write_push_memory(3 + int(Ind))
            else:  # Push index value on stack
                Self.write_get_pointerAD(Seg, Ind)  # get the pointer address
                # set the D register to the value of the pointer address
                Self.write_code("D=M")
                Self.write_pushD()  # push the value of the D register

        elif Com_Type == c_pop:  # The code for pushing and popping commands within the VM.
            if (debugpy):  # Hack files written in debug mode contain comments.
                # The D register value will be pushed on top of the Stack using self._WritePushD. Stacks are popped onto D by using self._WritePopD.
                Self.File.Write(" //POP %s %d \n" % (Seg, int(Ind)))
            if Seg == static:  # Pop index value from stack
                # pop the static memory
                Self.write_pop_memory(Self.static(Ind))
            elif Seg == pointer:  # Pop index value from stack
                # The code will assign the value of 2 to D, and then it will increment the value of Index by 1
                # At RAM address 3, we begin the TEMP segment
                Self.write_pop_memory(2 + int(Ind))
            elif Seg == temp:  # Pop index value from stack
                # The code will assign the value of 3 to D, and then it will increment the value of Index by 1
                Self.write_pop_memory(3 + int(Ind))
            else:  # Pop index value from stack
                Self.write_get_pointerAD(Seg, Ind)  # get the pointer address
                Self.write_popD()  # pop the value of the D register
                # set the value of the pointer address to the value of the D register
                Self.write_code("M=D, @R13, A=M")
        else:  # The code for pushing and popping commands within the VM.
            raise(
                "Invalid Push or Pop commamd added. Please ensure the command is correct." % Com_Type)  # raise the error message

    # This will write the Assembly Code for assorted Arithmetic Commands (Com for Command)
    def arithmetic(Self, Com):
        if (debugpy):  # When debugging, the hack file is written with comments.
            Self.File.write(" // %s \n" % Com)  # print the debug message
            # if the bottom two values are equal, then jump to the label
            if Com == add:  # Add the two top values on the stack and push the result on the stack.
                # add the two top values on the stack and push the result on the stack.
                Self.write_math2("+")
            elif Com == sub:  # Subtract the two top values on the stack and push the result on the stack.
                # subtract the two top values on the stack and push the result on the stack.
                Self.write_math1("-")
            # Bitwise OR of the two top values on the stack and push the result on the stack.
            elif Com == Or:
                # Bitwise OR of the two top values on the stack and push the result on the stack.
                Self.write_math2("|")
            # Bitwise AND of the two top values on the stack and push the result on the stack.
            elif Com == And:
                # Bitwise AND of the two top values on the stack and push the result on the stack.
                Self.write_math2("&")
            elif Com == negate:  # Negate the top value on the stack and push the result on the stack.
                # negate the top value on the stack and push the result on the stack.
                Self.write_math2("-")
            # Bitwise NOT of the top value on the stack and push the result on the stack.
            elif Com == Not:
                # Bitwise NOT of the top value on the stack and push the result on the stack.
                Self.write_math2("!")
            # Compare the two top values on the stack and push the result on the stack.
            elif Com == eq:
                Self.write_compare("jeq")  # jump if equal to the label
            # Compare the two top values on the stack and push the result on the stack.
            elif Com == gt:
                Self.write_compare("jgt")  # jump if greater than the label
            # Compare the two top values on the stack and push the result on the stack.
            elif Com == lt:
                Self.write_compare("jlt")  # jump if less than the label
        else:  # When not debugging, the hack file is written without comments.
            # raise the error message
            raise("Invalid Arithmetic Command - " + Com)

    # This will write the Assembly Code for assorted Arithmetic Commands (Com for Command)
    def write_math1(Self, Operator):
        # get the top two values on the stack
        Self.write_code("@SP")  # set the stack pointer to the top of the stack
        # set the stack pointer to the top of the stack
        Self.write_code("A=M-1")
        Self.write_code("M=M%sM" % (Operator))  # perform the math operation

    # This will write the Assembly Code for assorted Arithmetic Commands (Opr for Operator)
    def write_math2(Self, Operator):
        Self.write_code("@SP")  # set the stack pointer to the top of the stack
        Self.write_code("D=M")  # decrement the stack pointer
        # set the stack pointer to the top of the stack
        Self.write_code("A=A-1")
        # set the stack pointer to the top of the stack
        Self.write_code("A=A+1")
        Self.write_code("M=M%sD" % (Operator))  # perform the math operation
        Self.write_code("AM=M-1")  # decrement the stack pointer

    # This will write the Assembly Code for assorted Arithmetic Commands (JMP for Jump)
    def write_compare(Self, JMP):
        if JMP in Self.compute_labels:  # if the label is already in the dictionary
            # get the label from the dictionary
            objective = Self.compute_labels[JMP]
            return_address = Self.Label_Unique()  # get a new label called return_address
            # move the value to the D register
            Self.write_move_value(return_address, "R12")
            # jump to the label if the condition is true
            Self.write_code("0;JMP, @%s")
            Self.write_code("(%s)" %
                            (objective, return_address))  # write the label to the file and the return address
        else:  # if the label is not in the dictionary yet
            return_address = Self.Label_Unique()  # get a unique label called return_address
            # move the value to the D register and set the label to the return address
            Self.write_move_value(return_address, "R12")
            # write the label to the file and the return address
            Self.write_common_compare(JMP)
            # write the label to the file
            Self.write_code("(%s)" % (return_address))

    # This will write the common code for the compare commands (JMP for Jump)
    def write_common_compare(Self, JMP):
        # get the top two values on the stack and store them in the D and M registers
        if debugpy:
            # print the debug message to the file
            Self.File.Write(
                " // %s Common Code can be compared here \n" % (JMP))  # print the debug message
            write_Rack1 = False  # set the Rack-1 to false
            if not "Rack1" in Self.compute_labels:  # if the label is not added in the dictionary
                # get a unique label for Rack-1 and add it to the dictionary
                Self.compute_labels["Rack1"] = Self.Label_Unique()
                # get a unique label for Rack-2 and add it to the dictionary
                Self.compute_labels["Rack2"] = Self.Label_Unique()
            write_Rack1 = True  # set the Rack-1 to true if it is not already

        Label_0 = Self.Label_Unique()  # get a unique label called Label_0
        # add the label to the dictionary with the JMP command as the value
        Self.compute_labels[JMP] = Label_0
        # get the label for Rack-1 from the dictionary
        Label_1 = Self.compute_labels["Rack1"]
        # get the label for Rack-2 from the dictionary
        Label_2 = Self.compute_labels["Rack2"]
        # set the stack pointer to the top of the stack and store it in the D register
        Self.write_code("@SP \n A=M-1 \n D=M \n D=M-D \n A=A-1 \n")
        # jump to the label if the condition is true and set the stack pointer to the top of the stack
        Self.write_code("@%s \n D;J%s \n" % (Label_1, JMP))
        # jump to the label if the condition is false and set the stack pointer to the top of the stack
        Self.write_code("@%s \n D;J%s \n" % (Label_2, JMP))
        # write the label to the file and the return address
        Self.write_code("(%s)" % (Label_0))

        if write_Rack1:  # if the Rack-1 is not already written to the file
            if debugpy:  # if the debug flag is set to true
                # print the debug message to the file
                Self.File.Write(
                    " //  Common Code for Rack-1 can be compared here:  %s   \n")  # print the debug message for Rack-1
                # write the label to the file and the return address for Rack-1
                Self.write_code("(%s)" % Self.label_lcl["Rack-1"])

    def write_label(Self, Label):
        if debugpy:  # if the debug flag is set to true and the label is not already in the dictionary
            # print the debug message to the file and add the label to the dictionary
            Self.File.Write(" // %s Label \n")
            # write the label to the file and the return address for Rack-1
            Self.write_code("(%s)" % Self.label_lcl[Label])

    def write_goto(Self, Label):  # write the Assembly Code for the GOTO command
        if debugpy:  # if the debug flag is set to true and the label is not already in the dictionary
            # print the debug message to the file and add the label to the dictionary
            Self.File.Write(" // %s GOTO \n" % (Label))
        # write the label to the file and the return address for Rack-1
        Self.write_code("@%s \n 0;JMP \n" % (Self.label_lcl[Label]))

    def write_if(Self, Label):  # write the Assembly Code for the IF command (IFGOTO)
        if debugpy:  # if the debug flag is set to true and the label is not already in the dictionary
            # print the debug message to the file and add the label to the dictionary
            Self.File.Write(" // %s IF \n")
            # get the label from the dictionary for the IF command
            objective = Self.label_lcl[Label]

        """
            The code for the if-goto should be written based on the assumption:
                1. A location to jump to can be found in the variable 'target',
                2. Stacks contain a value at the top that leads to jumps if it is not zero.
        """

    # write the Assembly Code for the FUNCTION command (function declaration)
    def write_function(Self, Function_name, Number_Of_Locals):
        # set the function name to the variable Function_name
        Self.Function_name = Function_name
        if (debugpy):  # if the debug flag is set to true and the label is not already in the dictionary
            # print the debug message to the file and add the label to the dictionary for the function
            Self.File.Write(" // %s Function \n" %
                            (Function_name), (Number_Of_Locals))

        """
            The VM language command that implements the function must be coded to complete.
                1. Name the function with a label
                2. Place the stack of variables located locally on top of the sum of locals.
                3. The stack pointer (SP) is at the first local location as soon as the program starts. 
                    If the correct ML needs to be written multiple times, this can be achieved with a loop.
                    For example, for loops, Loop = Self._Label_Unique() the ML should be labelled.
        """

    def write_return(Self):  # write the Assembly Code for the RETURN command (function return)
        if debugpy:  # if the debug flag is set to true and the label is not already in the dictionary
            # print the debug message to the file and add the label to the dictionary for the function
            Self.File.Write(" // %s Return \n")
            # get the label from the dictionary for the function return
            if Self.ret_label != None:
                # write the label to the file and the return address for the function return
                Self.write_code("( % s)" % Self.ret_label)
            else:  # if the label is not in the dictionary yet
                # write the return label to the file and the return address for the function
                Self.write_code("0;JMP" % Self.ret_label)
                Self.write_common_ret()  # write the common code for the function return to the file

    # write the common code for the function return to the file (called by write_return)
    def write_common_ret(Self):
        if debugpy:  # if the debug flag is set to true and the label is not already in the dictionary and the function name is not None
            # print the debug message for the function return (called by write_return)
            Self.File.Write(" // Common Code for Function Return \n")
        # get a unique label for the function return and add it to the dictionary
        Self.ret_label = Self.Label_Unique()
        # write the label to the file and the return address for the function return
        Self.write_code("(%s)" % [Self.ret_label])

        """
            Based on the book and chapter 7 & 8 slides, write the following code to handle the return:
                1. Firsly, in addition to the code 'Self.write_code', I found it helpful to use the 'geeksforgeeks' and 'the elements of computing systems' guide to write the code.
                2. Secondly, functions such as 'Self.write_move_memory' here I found the top guides quite useful with other 7 websites to back up the code.
                3. Finally, I had to study/experiment on the functions and prepare a report which involved screenshots of the code, and end results from the VM Simulators.
        """
        Self.write_code(
            "D=M \n @R13 \n @5 \n A=D-A \n @LCL")  # get the value of the local variable at the top of the stack by returning the IP of the local variable
        # set the value of the local variable at the top of the stack to the value of the return address (R13)
        Self.write_code("@R13", "@M=D")
        Self.write_popD()  # pop the return address from the stack to the D register
        # set the return address to the value of the D register
        # set the return address to the value of the argument 0 (R13)
        Self.write_code("@M=D \n M=D \n @argumuent \n R14 \n")
        # set the stack pointer to the value of the local variable at the top of the stack
        Self.write_move_memory("lcl", "stack pointer", "R14")
        # pop the return value from the stack to the temp register (This)
        # and the local variable at the top of the stack (That)
        # and the argument at the top of the stack (argument)
        Self.write_pop_memory("That", "This", "argument", "lcl")

    # write the Assembly Code for the CALL command (function call)
    def write_call(Self, Function_name, Number_Of_Args):
        if debugpy:  # if the debug flag is set to true and the label is not already in the dictionary
            Self.File.Write(" // %s Call \n" %
                            (Function_name), (Number_Of_Args))  # print the debug message to the file and add the label to the dictionary for the function
        # get a unique label for the return address and add it to the dictionary
        return_address = Self.Label_Unique()
        # move the function name to the return address label - this is the return address for the function call
        Self.write_move_val(Function_name, "R14", Number_Of_Args, "R13")
        # write the label to the file and the return address for the function call (R13)
        Self.write_code("@%s \n 0;JMP \n" % (return_address))

        if Self.Call_label != None:  # if the label is not in the dictionary yet and the function name is not None
            # write the label to the file and the return address for the function call (R13)
            Self.write_code("(%s)" % Self.Call_label)
        else:  # if the label is not in the dictionary yet
            # write the return label to the file and the return address for the function call (R13)
            Self.write_code("(%s)" % Self.Call_label)
            # write the common code for the function call to the file (called by write_call)
            Self.write_common_call()
            # write the return address to the file and the return address for the function call (R13)
            Self.write_code("(%s)" % (return_address))

            """
                Instructions for the function call: According to the book and slides, I wrote the following code to handle the call.
                    1. In the method WriteCall, the following code has been removed.
                    2. It may also be helper function to use Self._write_code in conjunction with this, another helper function is Self.write_push_memory. It is very useful.
                    3. The jump to function address and lcl (local) and Arg (argument) must also be sent along with the 'frame.'
            """
   # write the common code for the function call to the file (called by write_call)
    def write_common_call(Self):
        if debugpy:  # if the debug flag is set to true and the label is not already in the dictionary
            Self.File.Write(" // Common Code for Function Call \n")
            # get a unique label for the function call and add it to the dictionary (dictionary means VM_Commands)
            Self.Call_label = Self.Label_Unique()
            # write the label to the file and the return address for the function call (R13)
            Self.write_code("(%s)" % (Self.Call_label))
            Self.write_pushD()  # push the return address to the stack (R13)
            # push the local variable, argument, This, and That to the stack (R13)
            Self.write_push_memory("lcl", "argument", "This", "That")
            # set the return address to the value of the return address (R13)
            Self.write_code("@SP \n M=M-1 \n A=M \n D=M \n @R13 \n M=D \n")
            Self.write_code(
                "@R13 \n M=D \n D=D-M \n @4 \n D=D-A \n @Argument \n")  # set the value of the argument to the value of the return address (R13)
            # jump to the function address
            Self.write_code("@R14 \n A=M \n 0;JMP \n")

    # get a unique label for the function return and add it to the dictionary
    def Label_Unique(Self):
        Self.number_of_labels += 1  # increment the number of labels by 1
        # return the label for the function return
        return "RETURN_%s" % (Self.number_of_labels)

        """
        Label functions/modules with unique names.
        File_name ##name will be used if no function is entered.
        A function_name#name is used if it does not exist.
        """
    def local(Self, Name):  # get a unique label for the local variable and add it to the dictionary
        # if the function name is not None (if the function is not None)
        if Self.Function_name != None:
            # return the label for the local variable in the function
            return Self.Function_name + "_" + Name
        else:  # if the function name is None (if the function is None)
            # return the label for the local variable in the file (not in the function)
            return Self.File_name + "_" + Name

        """
        'Index' should be named.
        Name_of_the_file.index will be its name.
        """
    def static(Self, Ind):  # get a unique label for the static variable and add it to the dictionary
        # return the label for the static variable in the file
        return Self.File_name + "_" + str(Ind)

    # write the code to the file (called by write_push, write_pop, write_call, write_function)
    def write_code(Self, Code):
        # increment the stack pointer by 1
        # replace the comma and semicolon with new lines and no semicolon
        Code = Code.replace(",", "\n").replace(";", "")
        # write the code to the file (called by write_push, write_pop, write_call, write_function)
        Self.File.write(Code + "\n")

    # write the code to push the return address to the stack (called by write_call)
    def write_pushD(Self):
        # increment the stack pointer by 1 and set the value of the stack pointer to the value of the return address
        Self.write_code("AM=M+1 \n M=D \n A=A-1 \n @SP \n")

    """
        Stack content from a memory location can be pushed using code.
        An address or identifier may be used as the label.
    """
    def write_push_memory(Self, Label):  # write the code to push the stack content from a memory location to the stack (called by write_call)
        # set the value of the stack pointer to the value of the memory location
        Self.write_code("D=M, @%s" (Label))
        # push the stack content from a memory location to the stack (called by write_call)
        Self.write_pushD()

    """
    Add a value to the stack immediately by writing code.
    In this case, the address of the identifier is pushed.
    """
    def write_push_val(Self, Value):  # write the code to push a value to the stack (called by write_call)
        if Value.isdigit() == "0":  # if the value is a number
            # push the value to the stack
            Self.write_code("@SP \n AM=M+1 \n A=A-1 \n M=0 \n")
        elif Value.isdigit() == "1":  # if the value is a boolean (true or false)
            # push the value to the stack (true)
            Self.write_code("@SP \n A=A-1 \n M=1 \n AM=M+1 \n")
        else:
            # if the value is a variable or a function
            Self.write_code("@%s \n D=A \n" % (Value))
            Self.write_code()  # push the value to the stack (called by write_call)

    def write_popD(Self):
        # decrement the stack pointer by 1 and set the value of the stack pointer to the value of the memory location
        Self.write_code("AM=M-1 \n D=M \n A=A-1 \n @SP \n")

    """
        Put a stack in memory by writing a piece of code.
        Many labels include identifiers, absolute addresses, and date identifiers.
    """
    def write_pop_memory(Self, Label):  # write the code to put a stack in memory (called by write_call)
        Self.write_popD()  # pop the stack content to the memory location (called by write_call)
        # set the value of the memory location to the value of the stack content (called by write_call)
        Self.write_code("M=D, @%s" % (Label))

    """
        The source code must be moved to the destination location with the code.
        An identifier or an absolute address may be used as 'Source Code' and 'Destination.'
    """
    def write_move_memory(Self, Source, Destination):  # write the code to move a stack in memory (called by write_call)
        # move the stack content to the memory location (called by write_call)
        Self.write_code("@%s \n D=M \n @%s \n M=D \n" % (Source, Destination))

    """
        'Self.write_code' relocates an instantaneous value into the memory address 'Destination.'
        The term 'destination' might refer to either identification or an exact address.
    """
    def write_move_val(Self, Value, Destination):  # write the code to move a value to the memory location (called by write_call)
        if Value.isdigit() == "0":  # if the value is a number (0)
            # set the value of the memory location to 0
            Self.write_code("@%s \n M=0 \n" % (Destination))
        elif Value.isdigit() == "1":  # if the value is a boolean (true or false)
            # set the value of the memory location to 1
            Self.write_code("@%s \n M=1 \n" % (Destination))
        else:  # if the value is a variable or a function
            # move the value to the memory location (called by write_call)
            Self.write_code("@%s \n D=A \n @%s \n M=D \n" %
                            (Value, Destination))

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
        if (int(Ind) == 0):  # This is the RAM segment and the index is 0.
            # This is the RAM segment and the index is 0 and the value is the value of the pointer.
            Self.write_code("AD=M \n @%s \n" % (POINTER, int(Ind)))
        # This is the RAM segment and the index is greater than 0.
        elif (int(Ind) > 0):
            # This is the RAM segment and the index is greater than 0 and the value is the value of the pointer.
            Self.write_code("AD=M+1 \n @%s \n" % (POINTER, int(Ind)))
        else:  # This is the RAM segment and the index is less than 0.
            # This is the RAM segment and the index is less than 0 and the value is the value of the pointer.
            Self.write_code("D=M \n AD=D+A \n @%s \n @%d \n " %
                            (POINTER, int(Ind)))
    debugpy = FALSE  # set the debug value to false for the next command
