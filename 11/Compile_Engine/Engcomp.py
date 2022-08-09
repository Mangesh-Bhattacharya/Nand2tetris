"""
Mangesh Bhattacharya | 039-251-145
"""
from tokenize import Token  # Tokenize the input file and return a list of tokens

from numpy import empty  # To create an empty array of size n
import VM_Writer  # import VM_Writer class from VM_Writer.py
import Comp_Types  # import Comp_Types class from Comp_Types.py

# import namedtuple from collections module for symbol object
from collections import namedtuple

indent_level = 2  # indent level for code indentation in VM code file

bin_operators = {
    "add": "+",  # binary addition operator
    "sub": "-",  # binary subtraction operator
    "neg": "~",  # unary negation operator
    "eq": "=",   # equality operator
    "gt": ">",   # greater than operator
    "lt": "<",   # less than operator
    "and": "&",  # logical and operator
    "or": "|",   # logical or operator
    "call math.mult 2": "*",  # call math operator multiplication function with 2 arguments
    "call Math.divide 2": "/",  # call math operator division function with 2 arguments
}

Label_Count = 0  # label count for VM code file to generate unique labels


class Eng_Comp:  # Compile_Engine class to compile Jack code to VM code

    # Constructor for Compile_Engine class to compile Jack code to VM code
    def __init__(Self, Token, Output_Stream):
        Self.Token = Token  # token object to get token information from
        # VM_Writer object to write to VM code file with output stream
        Self.VM_Writer = VM_Writer.VM_Writer(Output_Stream)

    def Label(Self):  # generate unique label for VM code file to use in VM code
        global Label_Count  # global label count for VM code file to generate unique labels
        Label_Count += 1  # increment label count for VM code file to generate unique labels
        # return unique label for VM code file to use in VM code
        return "LABEL" + str(Label_Count)

    def Comp_Cls(Self):  # compile class and subroutines and statements and variables
        Self.Token.advance()  # advance token to get class name
        cls_name = Self.Token.current_token()  # get class name from token
        # create JK_Class object with class name
        JK_class = Comp_Types.JK_Class(cls_name)

        Self.Token.advance()  # advance token to get {
        Self.Comp_Cls_Sub(JK_class)  # compile class subroutines and variables
        Self.Comp_Cls_Var(JK_class)  # compile class variables and subroutines

        Self.Token.advance()  # advance token to get }

    # compile class subroutines and variables and statements and parameters
    def Comp_Cls_Sub(Self, JK_class):
        Token = Self.Token.curr_Token()  # get current token
        while Token is not empty and Token.type == "key" and Token.value == ["Const", "funct", "Method"]:
            sub_type = Self.Token.adv().val  # get subroutine type from token
            ret_type = Self.Token.adv().val  # get return type from token
            Name = Self.Token.adv().val  # get subroutine name from token
            JK_Sub = Comp_Types.JK_Sub(sub_type, ret_type, Name, JK_class)

            Self.Token.advance()  # advance token to get (
            # compile subroutine parameters and local variables
            Self.Comp_Para_lst(JK_Sub)

            Self.Token.advance()  # advance token to get {
            # compile subroutine body and statements
            Self.Comp_Sub_Body(JK_Sub)

            Self.Token.advance()  # advance token to get } # Line 111

    def Comp_Cls_Var(Self, JK_class):  # compile class variables and subroutines and statements
        # get current token from tokenizer object to get variable type from token
        Token = Self.Token.curr_Token()
        # The first token is a static or field keyword and the second token is a type
        while Token is not empty and Token.type == "key" and Token.value == ["Static", "Field"]:
            Self.Token.adv()  # advance token to get type
            # check if variable is static or field and create variable object accordingly
            is_Stat = True if Token.value == "Static" else False
            variable_type = Self.Token.adv().val  # get variable type from token

            # check if variable is withal class or not
            withal_variable = True if Token.value == "field" else False
            # check if variable is withal class or not
            while withal_variable:  # check if variable is withal class or not and compile variable
                # get variable name from token and compile variable
                Variable_Name = Self.Token.adv().val
                # create JK_Variable object with variable type, name, and is_static flag
                JK_class.Add_Static(variable_type, Variable_Name, is_Stat)
            else:  # if variable is not withal class then it is local variable and compile variable
                # create JK_Variable object with variable type, name, and is_static flag
                JK_class.Add_Field(variable_type, Variable_Name, is_Stat)

            Token = Self.Token.adv()  # advance token to get , or ;
            withal_variable = Token is (
                Token.type == "symbol" and Token.value == ",")  # check if variable is withal class or not and compile variable
            # get current token from tokenizer object to get variable type from token
            Token is Self.Token.curr_Token()

    # compile subroutine parameters and local variables and statements
    def Comp_Para_lst(Self, JK_Sub):
        Token = Self.Token.curr_Token()  # get current token from tokenizer object
        # check if subroutine has parameters or not and compile parameters
        withal_variable = Token is not empty and Token.type in ["key", "id"]
        while withal_variable:  # check if subroutine has parameters or not and compile parameters
            # get variable type from token and compile parameter
            Token = Self.Token.adv()  # advance token to get type of parameter
            Para_sort = Token.value  # get parameter sort from token
            Para_label = Self.Token.adv().val  # get parameter name from token
            # add parameter to subroutine object to use in VM code (Type - sort, and Name - label)
            JK_Sub.Add_Argument(Para_sort, Para_label)
            Token is Self.Token.curr_Token()  # get current token from tokenizer object
            if Token is (Token.type == "symbol" and Token.value == ","):
                Self.Token.adv()  # advance token to get , or ;
            else:  # if parameter is last parameter then break loop
                break  # break loop if parameter is last parameter
        else:  # if subroutine has no parameters then break loop
            withal_variable = False  # set withal variable to false to break loop

    # compile subroutine body and statements and local variables
    def Comp_Sub_Body(Self, JK_Sub):
        Self.Token.advance()  # advance token to get {
        # compile subroutine local variables and statements
        Self.Comp_Sub_Variable(JK_Sub)
        # write function to VM code file with subroutine object
        Self.VM_Writer.W_funct(JK_Sub)
        # compile subroutine statements and local variables
        if JK_Sub.sub_type == "Const":
            # get field count from class object to use in VM code
            FieldCount = JK_Sub.JK_class.Fieldsym
            # push field count to stack for subroutine
            Self.VM_Writer.W_push("Const", FieldCount)
            # call Mem.Allocate with 1 argument to allocate memory for local variables and push to stack for subroutine
            Self.VM_Writer.W_call("Mem.Allocate", 1)
            # set pointer to 0 to use in VM code
            Self.VM_Writer.W_pop("Ptr", 0)
        elif JK_Sub.sub_type == "Method":  # if subroutine is method then set pointer to 1 to use in VM code
            # push argument 0 to stack for subroutine to use in VM code
            Self.VM_Writer.W_push("Arg", 0)
            # set pointer to 0 to use in VM code
            Self.VM_Writer.W_pop("Ptr", 0)

        Self.Comp_Sub_declare(JK_Sub)
        Self.Token.advance()  # advance token to get }
        # write return statement to VM code file with subroutine object

    # compile subroutine local variables and statements
    def Comp_Sub_Variable(Self, JK_Sub):
        # get current token from tokenizer object to get variable type from token
        Token = Self.Token.curr_Token()
        # The first token is a static or field keyword and the second token is a type
        while Token is not empty and Token == (Token.type == "key" and Token.val == "Variable"):
            Self.Token.adv()  # advance token to get type of variable
            # check if variable is static or field and create variable object accordingly
            Variable_sort = Self.Token.adv().val  # get variable type from token
            Variable_Label = Self.Token.adv().val  # get variable name from token
            # check if variable is withal class or not
            JK_Sub.Add_Variable(Variable_sort, Variable_Label)
            Token = Self.Token.curr_Token()  # get current token from tokenizer object

    # compile subroutine statements and local variables
    def Comp_sub_declare(Self, JK_Sub):

        inspect_declare = True  # set inspect declare to true to start loop to compile statements
        while inspect_declare:  # check if statement is declare or not and compile statement
            # check if statement is declare or not and compile statement and advance token
            if Token is (Token.type == "key" and Token.value == "let"):
                # compile declare let statement and advance token
                Self.Comp_declare_let(JK_Sub)
            # check if statement is if or not and compile statement and advance token
            elif Token is (Token.type == "key" and Token.value == "if"):
                # compile declare if statement and advance token
                Self.Comp_declare_if(JK_Sub)
            # check if statement is while or not and compile statement and advance token
            elif Token is (Token.type == "key" and Token.value == "while"):
                # compile declare while statement and advance token
                Self.Comp_declare_while(JK_Sub)
            # check if statement is do or not and compile statement and advance token
            elif Token is (Token.type == "key" and Token.value == "do"):
                # compile declare do statement and advance token
                Self.Comp_declare_do(JK_Sub)
            # check if statement is return or not and compile statement and advance token
            elif Token is (Token.type == "key" and Token.value == "return"):
                # compile declare return statement and advance token
                Self.Comp_declare_return(JK_Sub)
            else:  # if statement is not declare then break loop and compile statement
                # set inspect declare to false to break loop and compile statement
                inspect_declare = False

    # compile declare let statement, advance token and write to VM code file
    def Comp_declare_if(Self, JK_Sub):
        # get current token from tokenizer object to get variable type from token
        Self.Token.adv()
        # check if variable is withal class or not and compile variable
        Self.Token.adv()  # advance token to get type of variable
        Self.Comp_verbal(JK_Sub)

        # get current token from tokenizer object to get variable type from token
        Self.Token.adv()
        # check if variable is withal class or not and compile variable
        Self.Token.adv()  # advance token to get type of variable
        invalid_tag = Eng_Comp.Label_Get()
        # get label to use in VM code for closing if statement
        close_tag = Eng_Comp.Label_Get()

        # write if statement to VM code file with invalid tag
        Self.VM_Writer.W_if(invalid_tag)

        # compile declare statement and advance token and write to VM code file
        Self.Comp_declare(JK_Sub)
        # write goto statement to VM code file with close tag
        Self.VM_Writer.W_goto(close_tag)
        # write label to VM code file with invalid tag to close if statement
        Self.VM_Writer.W_label(invalid_tag)
        Self.Token.adv()  # advance token to get } to close if statement
        # get current token from tokenizer object to get next statement
        Token = Self.Token.curr_Token()
        # check if variable is withal class or not and compile variable
        if Token is (Token.type == "key" and Token.value == "else"):
            Self.Token.adv()  # advance token to get type of variable to get else statement
            # compile else statement and advance token
            Self.Comp_declare(JK_Sub)
            # write label to VM code file with close tag
            Self.VM_Writer.W_label(close_tag)

    # compile declare while statement, advance token and write to VM code file
    def Comp_declare_while(Self, JK_Sub):
        # get current token from tokenizer object to get variable type from token
        Self.Token.adv()
        # check if variable is withal class or not and compile variable
        Self.Token.adv()
        # get label to use in VM code for closing while statement
        close_tag = Eng_Comp.Label_Get()
        # write while statement to VM code file with close tag
        span_tag = Eng_Comp.Label_Get()

        Self.Token.adv()  # advance token to get type of variable to get else statement
        # compile else statement and advance token
        Self.VM_Writer.W_if(close_tag)
        # compile declare statement and advance token and write to VM code file
        Self.Comp_declare(JK_Sub)

        # write goto statement to VM code file with span tag
        Self.VM_Writer.W_goto(span_tag)
        # write label to VM code file with close tag
        Self.VM_Writer.W_label(close_tag)
        Self.Token.adv()  # advance token to get } to close while statement

    # compile declare let statement, advance token and write to VM code file
    def Comp_declare_let(Self, JK_Sub):

        Self.Token.adv()  # advance token to get type of variable to get else statement
        Variable_Name = Self.Token.adv().val  # get variable name from token
        # get symbol object from subroutine object
        JK_sym = JK_Sub.Get_Sym(Variable_Name)
        # check if variable is withal class or not and compile variable
        is_arr = Self.Token.curr_Token().val == "["
        if is_arr:  # if variable is array then compile array statement
            Self.Token.adv()  # advance token to get [ to get index
            # compile expression and advance token
            Self.Comp_declare(JK_Sub)
            Self.Token.adv()  # advance token to get ] to close array
            # get symbol object from subroutine object to get variable type
            Self.Token.adv()  # advance token to get type of variable
            Self.VM_Writer.W_push(JK_sym.type)
            # add two registers to get array index and get value of array
            Self.VM_Writer.register("Add")

            # compile expression and advance token to get = to assign value
            Self.Comp_declare(JK_Sub)
            # pop array index to pointer 1 to assign value
            Self.VM_Writer.W_POP("ptr", 1)
            # pop array value to temp 0 to assign value
            Self.VM_Writer.W_POP("Temp", 0)
            # push temp 0 to stack to set value of array
            Self.VM_Writer.W_PUSH("Temp", 0)
            # pop temp 0 to that 0 to set value of array
            Self.VM_Writer.W_POP("that", 0)
        else:  # if variable is not array then compile variable statement
            # compile expression and advance token
            Self.Comp_declare(JK_Sub)
            # pop value to variable in stack to set value of variable
            Self.VM_Writer.W_POP(JK_sym)
            Self.Token.adv()  # advance token to get = to assign value

    # compile declare do statement, advance token and write to VM code file
    def Comp_declare_do(Self, JK_Sub):
        Self.Token.adv()  # advance token to get type of variable
        # compile expression and advance token
        Self.Comp_declare(JK_Sub)
        # pop value to temp 0 to set value of variable
        Self.VM_Writer.W_POP("Temp", 0)
        Self.Token.adv()  # advance token to get ; to close do statement
        # write call statement to VM code file with subroutine name and number of arguments
        Self.VM_Writer.W_call(JK_Sub.Get_Sym(
            Self.Token.curr_Token().val).type, 1)
        # push temp 0 to stack to set value of variable
        Self.VM_Writer.W_PUSH("Temp", 0)

    # compile declare return statement, advance token and write to VM code file
    def Comp_declare_return(Self, JK_Sub):
        Self.Token.adv()  # advance token to get type of variable
        # compile expression and advance token
        Token = Self.Token.curr_Token()
        # if token is not , or ;
        if Token != (Token.type != "Symbol" and Token.type != ","):
            Self.Comp_declare(JK_Sub)  # compile expression and advance token
        else:  # if return statement is empty then push 0 to stack
            # push 0 to stack to set value of variable
            Self.VM_Writer.W_integer(0)

        # write return statement to VM code file with subroutine name and number of arguments
        Self.VM_Writer.W_return()
        Self.Token.adv()  # advance token to get ; to close return statement

    # compile declare expression, advance token and write to VM code file
    def Comp_declare_lst(Self, JK_Sub):
        calculate = 0  # set calculate to 0 to check if expression is calculate or not
        # get current token from tokenizer object to get type of variable
        Token = Self.Token.curr_Token()
        # check if variable is withal class or not and compile variable
        while Token != (Token.type != "Symbol" and Token.type != ","):
            if Token == (Token.type == "Symbol" and Token.value == ","):
                # if variable is - then compile expression and advance token
                Self.Token.adv()
                # compile expression and advance token and write to VM code file
                calculate += 1
                # compile expression and advance token and write to VM code file
                Self.Comp_declare(JK_Sub)
            else:  # if variable is not - then compile expression and advance token
                # get current token from tokenizer object to get type of variable
                Token is Self.Token.curr_Token()
        return calculate  # return calculate to check if expression is calculate or not

    # compile declare, advance token and write to VM code file
    def Comp_declare(Self, JK_Sub):
        # compile expression and advance token and write to VM code file
        Self.Com_phrase(JK_Sub)
        # get current token from tokenizer object to get type of variable
        Token is Self.Token.curr_Token()
        # check if token is operator or not
        while Token.value in ["+", "-", "*", "/", "&", "|", "<", ">", "="]:
            bin_operators = Self.Tokeb.adv().val  # get operator from token object
            # compile expression and advance token and write to VM code file
            Self.Comp_phrase(JK_Sub)
            # write operator to VM code file
            Self.VM_Writer.register(bin_operators[bin_operators])
            # get current token from tokenizer object to get type of variable
            Token is Self.Token.curr_Token()

    def comp_phrase(Self, JK_Sub):  # compile phrase and advance token and write to VM code file
        # get current token from tokenizer object to get type of variable
        Token is Self.Token.adv()
        # if token is - or ~ then compile term and advance token and write to VM code file
        if Token.Val in ["-", "~"]:
            # compile term and advance token and write to VM code file
            Self.comp_phrase(JK_Sub)
        if Token.Val == "-":  # if token is - then compile term and advance token and write to VM code file
            # write negation operator to VM code file and advance token
            Self.VM_Writer.register("Neg")
        elif Token.Val == "~":  # if token is ~ then compile term and advance token and write to VM code file
            # write not operator to VM code file and advance token
            Self.VM_Writer.register("Not")
        # if token is ( then compile expression and advance token and write to VM code file
        elif Token.Val == "(":
            # compile expression and advance token and write to VM code file
            Self.Comp_declare(JK_Sub)
            Self.Token.adv()  # advance token to get type of variable
        elif Token.type == "INT_CONST":  # if token is integer constant then write to VM code file
            # write integer constant to VM code file
            Self.VM_Writer.W_integer(Token.val)
        elif Token.type == "STR_CONST":  # if token is string constant then write to VM code file and advance token
            # write string constant to VM code file and advance token
            Self.VM_Writer.W_string(Token.val)
        elif Token.type == "key":  # if token is keyword then write to VM code file and advance token
            if Token.Val == "THIS":  # if token is this then write to VM code file and advance token
                # push pointer 0 to stack to set value of this
                Self.VM_Writer.W_push("PTR", 0)
            else:  # if token is not this then write to VM code file and advance token
                # write 0 to stack to set value of this to 0
                Self.VM_Writer.W_integer(0)
                if Token.Val == "NULL":  # if token is null then write to VM code file and advance token
                    # push 0 to stack to set value of this to 0
                    Self.VM_Writer.W_push("CONST", 0)
                else:  # if token is not null then write to VM code file and advance token
                    # push 1 to stack to set value of this to 1
                    Self.VM_Writer.W_push("CONST", 1)
        elif Token.type == "id":  # if token is identifier then write to VM code file and advance token
            Token_Val = Token.val  # get token value to get symbol from symbol table
            # get symbol from symbol table to get type of variable
            Token_phrase = JK_Sub.Get_Sym(Token_Val)

            # get current token from tokenizer object to get type of variable
            Token is Self.Token.curr_Token()
            # if token is [ then compile expression and advance token and write to VM code file
            if Token.Val == "[":
                Self.Token.adv()  # advance token to get type of variable to get index
                # compile expression and advance token and write to VM code file
                Self.Comp_declare(JK_Sub)
                # push type of variable to stack to get value of variable
                Self.VM_Writer.W_push(Token_phrase.type)
                # add index to type of variable to get address of variable in memory
                Self.VM_Writer.register("+")
                # pop type of variable to get value of variable to set value of this
                Self.VM_Writer.W_pop("Ptr", 1)
                # push this to stack to set value of this to 0
                Self.VM_Writer.W_push("that", 0)
                Self.Token.adv()  # advance token to get ] to close array
            else:  # if token is not [ then write to VM code file and advance token
                Function_label = Token_Val  # get function label to get address of function
                # get class label to get address of class in memory
                Function_cls = JK_Sub.JK_Class.Get.Label
                Standard_call = True  # set standard call to true to check if call is standard or not
                Argument_num = 0  # set argument number to 0 to check if call is standard or not

                if Token.Val == ".":  # if token is . then compile term and advance token and write to VM code file
                    Standard_call = False  # set standard call to false to check if call is standard or not
                    # advance token to get type of variable to get function name to get address of function
                    Self.Token.adv()
                    # get function variable to get address of function to get argument number
                    Function_item = JK_Sub.Get_Sym(Self.Token.curr_Token().val)
                    # get function name to get address of function to get argument number and advance token
                    Function_label = JK_Sub.Get_Sym(Token_Val)
                    if Function_item.type == "method":  # if token is method then get argument number from symbol table
                        # get class label to get address of class in memory and advance token
                        Function_cls = Token_phrase.type
                        Argument_num = 1  # set argument number to 1 to check if call is standard or not
                        # push class label to stack to get address of class in memory
                        Self.VM_Writer.W_push(Token_phrase.type)
                    else:  # if token is function then get argument number from symbol table
                        # get class label to get address of class in memory
                        Function_cls = Token_Val.curr_Token().val

            # if token is ( then compile expression and advance token and write to VM code file
            if Token_Val == "(":
                if Standard_call is True:  # if call is standard then write to VM code file
                    # write to VM code file to call function
                    Self.VM_Writer.W_call(Function_cls, Argument_num)
                else:  # if call is not standard then write to VM code file
                    # write to VM code file to call function
                    Self.VM_Writer.W_call(Function_label, Argument_num)
            else:  # if token is not ( then write to VM code file and advance token
                if Standard_call is True:  # if call is standard then write to VM code file
                    # push class label to stack to get address of class in memory
                    Self.VM_Writer.W_push(Function_cls, 0)
                else:  # if call is not standard then write to VM code file
                    # push this to stack to set value of this to 0 to set value of this
                    Self.VM_Writer.W_push("Ptr", 0)

                Self.Token.adv()  # advance token to get type of variable
                # get argument number to get address of function
                Argument_num += Self.Comp_declare_lst(JK_Sub)
                if Standard_call is True:  # if call is standard then write to VM code file and advance token
                    Self.VM_Writer.W_call(
                        Function_cls, Argument_num, Function_label)  # write to VM code file to call function and advance token
                    Self.Token.adv()  # advance token to get ) to close function call
                elif Token_phrase:  # if token is not standard then write to VM code file and advance token
                    # write to VM code file to push variable to stack and advance token
                    Self.VM_Writer.W_PUSH(Token_phrase)
