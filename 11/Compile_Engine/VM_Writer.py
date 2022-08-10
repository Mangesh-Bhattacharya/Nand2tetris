################################################################################################
"""
    Name: Mangesh Bhattacharya 
    Course: Computer Fundamentals
    Code: DCN 250
    Inst: Dr. Yousef Ashibani
"""
################################################################################################

Seg_Kind = {  # Segment to index in memory array
    "Field": "this",  # this, that, pointer, temp or constant
    "Static": "static",  # static or constant
    "Argument": "argument",  # argument or constant or temp
    "Variable": "local"  # local or constant or temp or pointer
}


class VM_Writer:  # VM_Writer class to write the VM code to a file

    def __init__(Self, Output_Stream):  # Constructor for VM_Writer class
        Self.Output_Stream = Output_Stream  # Output stream to write to file
        Self.Lab_Count = 0  # Label count for if-goto command

    def W_if(Self, Lab):  # if-goto command
        # if-goto <label> (jump to label)
        Self.Output_Stream.write("if-goto {}\n".format(Lab))
        Self.Output_Stream.write("NOT \n")  # neg to jmp if false

    def W_goto(Self, Lab):  # Goto Command for if-goto command to jump to label
        # goto label from current line
        Self.Output_Stream.write("goto {}\n".format(Lab))

    def W_label(Self, Lab):  # Label Command for if-goto command to jump to label
        # label command for if-goto command to jump to label from current line
        Self.Output_Stream.write("label {}\n".format(Lab))

    def W_funct(Self, jk_sub):  # Function command to define a function in the VM code file
        cls_name = jk_sub.J__cls__.__Name__  # get class name from class object
        Name = jk_sub.Name  # Name of function to call
        lcl_variables = jk_sub.variable_sym  # local variables in the function scope
        # subroutine type in the function scope (method, function, constructor)
        sub_type = jk_sub.sub_type

        Self.Output_Stream.write(
            "Function {}.{} {}\n".format(cls_name, Name, lcl_variables))  # write function command to file with class name, function name, and local variables

    def W_ret(Self):  # Return command to return from a function in the VM code file
        # write return command to file to return from a function in the VM code file
        Self.Output_Stream.write("return\n")

    # Call command to call a function in the VM code file with class name, function name, and argument count
    def W_call(Self, Cls_Name, Func_Name, Arg_Count):
        Self.Output_Stream.write(
            "call {0}.{1} {2}\n".format(Cls_Name, Func_Name, Arg_Count))  # write call command to file with class name, function name, and argument count to call function

    def W_push(Self, jk_sym):  # Push command to push a variable in the VM code file to the stack
        value = jk_sym.value  # get value from symbol object
        balance = jk_sym.id  # get balance from symbol object

        Seg = value_seg(value)  # get segment from value
        # write push command to file with segment and balance to push value to stack
        Self.W_push(Seg, balance)

    def W_pop(Self, jk_sym):  # Pop command to pop value from stack to a variable in the VM code file
        # get value from symbol object (local, argument, static, this, that, pointer, temp)
        value = jk_sym.value
        balance = jk_sym.id  # get balance from symbol object to pop value from stack
        Seg = value_seg(value)  # get segment from value
        # write pop command to file with segment and balance to pop value from stack
        Self.W_pop(Seg, balance)

    # Push constant command to push a constant in the VM code file to the stack
    def W_push_const(Self, Seg, balance):
        # write push constant command to file with segment and balance to push constant to stack
        Self.Output_Stream.write("push {0} {1}\n".format(Seg, balance))

    # Pop constant command to pop a constant from the stack to a variable in the VM code file
    def W_pop_const(Self, Seg, balance):
        # write pop constant command to file with segment and balance to pop constant from stack
        Self.Output_Stream.write("pop {0} {1}\n".format(Seg, balance))

    def Write(Self, steps):  # Write command to write a command to the VM code file from the parser steps
        # write steps to file in VM code file as a string with a new line
        Self.Output_Stream.write("{}\n".format(steps))

    # Write command to write an integer to the VM code file from the parser steps
    def W_integer(Self, Num):
        # write push command to file with segment and balance to push integer to stack
        Self.Write_PUSH(Seg_Kind["Constant"], Num)

    def W_str(Self, m):  # Write command to write a string to the VM code file from the parser steps
        m = m[1: -1]  # remove quotes from string m to get string without quotes
        # write push command to file with segment and balance to push string length to stack
        Self.W_integer(len(m))
        # call String.new to create a new string object with length of string
        Self.W_call("String", "new", 1)
        for i in m:  # for each character in string m write push command to file with segment and balance to push character to stack
            # get ordinal value of character i to push to stack as integer value
            Self.W_integer(ord(i))
            # call String.addChar to add character to string object on top of stack to add to string
            Self.W_call("String", "addChar", 2)
