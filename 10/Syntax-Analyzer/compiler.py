import keyword
from os import stat
import string
from numpy import character, empty
from Grammar import grammar  # Grammar class from Grammar.py file

from Tokens.Tok_type import *  # Tokens from Tokens.Tok_type.py file
# Tokenizer class from Tokens.Tokenizer.py file
from Tokens.Tokenizer import tokenizer
from Tokens.key import key  # Keywords from Tokens.key.py file

# Symbol Table from Variables.Sym_Tab.py file
from Variables.Sym_Tab import Sym_Tab
# Variable Types from Variables.var_type.py file
from Variables.var_type import var_type

# Command class from Code_Gen.Command.py file
from Code_Gen.Command import Command, command
# VM_Writ class from Code_Gen.VM_Writ.py file
from Code_Gen.VM_Writ import VM_Writ
# Segment enum type from Code_Gen.Segment.py file
from Code_Gen.Segment import Seg, Segment

# Syntax_Exception from Syntax_Exception.Syntax_Ex.py file
from Syntax_Exception.Syntax_Ex import syntax_error_except

import Constant  # Constant class from Constant.py file


class compile_eng:  # Compile Engine class from Compile_Engine.py file

    # Constructor of Compile Engine class from Compile_Engine.py file
    def __init__(Self, Token, Out_File):
        Self.Token = Token  # Tokenizer object from Tokens.Tokenizer.py file
        Self.sym_tab = Sym_Tab()  # Symbol Table object from Variables.Sym_Tab.py file
        # VM_Writ object from Code_Gen.VM_Writ.py file
        Self.VM_Writ = VM_Writ(Out_File)

        Self.Name = "   "  # Name of the program
        Self.Step = 1  # Step of the program

        Self.Para_Count = 0  # Count of the parameters of the function
        Self.Local_Var_Count = 0  # Count of the local variables of the function

        Self.Subroute_Name = None  # Name of the subroute of the function
        Self.Subroute_Type = None  # Type of the subroute of the function

    def Compile(Self):  # Compile function from Compile_Engine.py file
        Self.Token.Adv()  # Advance the tokenizer object to the first token of the program

        # Check if the first token is a program keyword
        if Self.Token.Cur_Tok.type is Tok_type.key and Self.Token.key_word() is key.prg:
            Self.pace += 1  # Increase the pace of the program
        else:  # If the first token is not a program keyword
            # Raise a syntax error exception
            raise syntax_error_except(Self.pace, "Class")

        Self.Token.Adv()  # Advance the tokenizer object to the second token of the program

        if Self.Token.Cur_Tok.type is Tok_type.id:  # If the second token is an identifier token
            Self.Name = Self.Token.id()  # Get the name of the program from the tokenizer object and save it to the Name variable of the Compile Engine class object from Compile_Engine.py file
            Self.pace += 1  # Increase the pace of the program
        else:  # If the second token is not an identifier token
            # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
            raise syntax_error_except(Self.pace, "Identifier")

        Self.Token.Adv()  # Advance the tokenizer object to the third token of the program

        # If the third token is a '{' symbol token
        if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is '{':
            # Increase the pace of the program and save it to the pace variable of the Compile Engine class object from
            # Compile_Engine.py file from the tokenizer object from Tokens.Tokenizer.py file and save it to the pace variable of the
            # Compile Engine class object from Compile_Engine.py file from the tokenizer object from Tokens.Tokenizer.py file
            Self.pace += 1
        else:  # If the third token is not a '{' symbol token
            # Raise a syntax error exception and print the line number of the token
            # that caused the error and the token that caused the error in the source code file
            raise syntax_error_except(Self.pace, "{")

        Self.Token.Adv()  # Advance the tokenizer object to the fourth token of the program

        # If the fourth token is a '}' symbol token and the name of the program is not empty string
        if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is '}':
            # Increase the pace of the program and save it to the pace variable of the Compile Engine class object from
            # Compile_Engine.py file from the tokenizer object from Tokens.Tokenizer.py file and save it to the pace variable of the
            # Compile Engine class object from Compile_Engine.py file from the tokenizer object from Tokens.Tokenizer.py file
            Self.pace += 1
        else:  # If the fourth token is not a '}' symbol token or the name of the program is empty string
            # Raise a syntax error exception and print the line number of the token
            raise syntax_error_except(Self.pace, "}")

    def Var_Decl(Self):  # Variable Declaration function from Compile_Engine.py file
        # While the tokenizer object is a keyword token and the keyword is a variable keyword
        while Self.Token.Tok_type() is Tok_type.key and Self.Variable(Self.Token.key()):
            # Get the value of the variable keyword from the tokenizer object and
            # save it to the Value variable of the variable declaration function from Compile_Engine.py file from the tokenizer object from
            # Tokens.Tokenizer.py file and save it to the Value variable of the variable declaration function from Compile_Engine.py
            # file from the tokenizer object from Tokens.Tokenizer.py file
            Value = var_type(Self.Token.key().Val)
            # Create an empty array of type object to save the type of the variable from the tokenizer object from
            # Tokens.Tokenizer.py file and save it to the Type variable of the variable declaration function from
            # Compile_Engine.py file from the tokenizer object from Tokens.Tokenizer.py file
            Type = empty(1, dtype=object)
            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

            # If the next token is a keyword token and the keyword is a default keyword and the variable keyword is a variable keyword
            if Self.Token.Tok_type() is Tok_type.key and Self.Default(Self.Token.key().Val):
                # Get the value of the default keyword from the tokenizer object and save it to the Value variable of the variable declaration function from
                # Compile_Engine.py file from the tokenizer object from Tokens.Tokenizer.py file
                Value = Self.Token.key().Val
                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
            elif Self.Token.Tok_type() is Tok_type.id:  # If the next token is an identifier token and the variable keyword is a variable keyword and the default keyword is not a default keyword
                # Get the value of the identifier token from the tokenizer object and save it to the Value variable of the variable declaration function from
                # Compile_Engine.py file from the tokenizer object from Tokens.Tokenizer.py file
                Value = Self.Token.id()
                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
            else:  # If the next token is not a keyword token or the variable keyword is not a variable keyword or the default keyword is a default keyword
                # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
                raise syntax_error_except(Self.pace, "Value is incorrect")

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

            if Self.Token.Tok_type() is Tok_type.id:
                # Call the Def_Var function from Compile_Engine.py file
                Self.Def_Var(Self.Token.id(), Value, Type)
                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
            else:  # If the next token is not an identifier token
                # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
                raise syntax_error_except(Self.pace, "Add you variable name")

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

            # While the next token is a ',' symbol token and the variable keyword is a variable keyword and the default keyword is not a default keyword and
            # the identifier token is not an empty string and the identifier token is not a reserved word token and
            # the identifier token is not a variable keyword token and the identifier token is not a default keyword token and
            # the identifier token is not a ')' symbol token and the identifier token is not a ']' symbol token and the identifier token is not a '}' symbol token
            while Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is ',':
                # Increase the pace of the program by 1 to move to the next token in the source code file in the source code file and
                # save it to the pace variable of the Compile Engine class object from Compile_Engine.py file from the tokenizer object from Tokens.Tokenizer.py file and
                Self.pace += 1

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

            if Self.Token.Tok_type() is Tok_type.id:  # If the next token is an identifier token and the variable keyword is a variable keyword and the default keyword is not a default keyword
                # Call the Def_Var function from Compile_Engine.py file and save the identifier token from the tokenizer object from Tokens.Tokenizer.py file
                Self.Def_Var(Self.Token.id(), Value, Type)
                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
            else:  # If the next token is not an identifier token
                # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
                raise syntax_error_except(Self.pace, "Add you variable name")

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

            # If the next token is a ';' symbol token and the variable keyword is a variable keyword and the default keyword is not a default keyword
            if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is ';':
                # Increase the pace of the program by 1 to move to the next token in the source code file in the source code file and
                # save it to the pace variable of the Compile Engine class object from Compile_Engine.py file from the tokenizer object from Tokens.Tokenizer.py file and
                Self.pace += 1
            else:  # If the next token is not a ',' symbol token
                # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
                raise syntax_error_except(Self.pace, ";")

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

    def subroute_decl(Self):  # Subroute Declaration function from Compile_Engine.py file
        while Self.Token.Tok_type() is Tok_type.key and Self.Subroute(Self.Token.key()):
            Value = empty  # Create an empty array of type object to save the type of the variable from the tokenizer object from Tokens.Tokenizer.py file
            Self.Sub_Name = "   "  # Create an empty string to save the name of the subroute from the tokenizer object from Tokens.Tokenizer.py file
            # Save the type of the subroute from the tokenizer object from Tokens.Tokenizer.py file to the Subroute_Type variable of the
            Self.Subroute_Type = Self.Token.key()

            # Begin a new subroutine scope in the symbol table from the symbol table object from Symbol_Table.py file
            Self.sym_tab.begin_subroutine()

            if Self.Token is keyword.Method:  # If the next token is a keyword token and the keyword is a method keyword and the subroute keyword is a subroute keyword
                # Define the this variable in the symbol table from the symbol table object from Symbol_Table.py file
                Self.sym_tab.define("this", Self.Name, var_type.ARG)
                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

            if Self.Token.Tok_type() is Tok_type.key and Self.Default(Self.Token.key().Val) or Self.Token.key() is key.Void:
                # Save the type of the subroute from the tokenizer object from Tokens.Tokenizer.py file to the Value variable
                Value = Self.Token.key().Val
                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
            # If the next token is an identifier token and the subroute keyword is a subroute keyword
            elif Self.Token.Tok_type() is Tok_type.id:
                # Save the type of the subroute from the tokenizer object from Tokens.Tokenizer.py file to the Value variable
                Value = Self.Token.id()
                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
            else:  # If the next token is not a keyword token or the subroute keyword is not a subroute keyword
                # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
                raise syntax_error_except(Self.pace, "Add you subroute type")

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

            # If the next token is an identifier token and the subroute keyword is a subroute keyword
            if Self.Token.Tok_type() is Tok_type.id:
                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
                # Save the name of the subroute from the tokenizer object from Tokens.Tokenizer.py file to the Sub_Name variable
                Self.Subroute_Name = Self.Token.id()
            else:
                # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
                raise syntax_error_except(Self.pace, "Add you subroute name")

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

            # If the next token is a '(' symbol token and the subroute keyword is a subroute keyword
            if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is '(':
                # Increase the pace of the program by 1 to move to the next token in the source code file in the source code file and
                # save it to the pace variable of the Compile Engine class object from Compile_Engine.py file from the tokenizer object from Tokens.Tokenizer.py file and
                Self.pace += 1
            else:  # If the next token is not a '(' symbol token
                # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
                raise syntax_error_except(Self.pace, "(")

            Self.Compilation_List()  # Call the Compilation_List function from Compile_Engine.py file

            if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is ')':
                # Increase the pace of the program by 1 to move to the next token in the source code file in the source code file and
                # save it to the pace variable of the Compile Engine class object from Compile_Engine.py file from the tokenizer object from Tokens.Tokenizer.py file and
                Self.pace += 1
            else:  # If the next token is not a ')' symbol token
                # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
                raise syntax_error_except(Self.pace, ")")

            # Call the Complization_List function from Compile_Engine.py file
            Self.Compilation_SubrouteBody()

    def Compilation_List(Self):  # Compilation List function from Compile_Engine.py file
        Self.Token.Adv()  # Advance the tokenizer object to the next token of the program
        # If the next token is a ')' symbol token and the subroute keyword is a subroute keyword
        if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is ')':
            return  # Return from the Compilation_List function from Compile_Engine.py file
        else:  # If the next token is not a ')' symbol token
            Value = var_type.ARG  # Create a variable of type var_type to save the type of the variable from the tokenizer object from Tokens.Tokenizer.py file
            type = empty  # Create an empty array of type object to save the type of the variable from the tokenizer object from Tokens.Tokenizer.py file

            # If the next token is a keyword token and the keyword is a keyword token and the subroute keyword is a subroute keyword
            if Self.Token.Tok_type() is Tok_type.key and Self.Default(Self.Token.key().Val):
                # Save the type of the subroute from the tokenizer object from Tokens.Tokenizer.py file to the Value variable
                Value = Self.Token.key().Val
                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
            elif Self.Token.Tok_type() is Tok_type.id:
                # Save the type of the subroute from the tokenizer object from Tokens.Tokenizer.py file to the Value variable
                Value = Self.Token.id()
                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
            else:  # If the next token is not a keyword token or the subroute keyword is not a subroute keyword
                # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
                raise syntax_error_except(
                    Self.pace, "Value is not a keyword or identifier")

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

            if Self.Token.Tok_type() is Tok_type.id:  # If the next token is an identifier token then
                # Save the name of the variable from the tokenizer object from Tokens.Tokenizer.py file to the Name variable
                Self.Define_Variable(Self.Token.id(), Value, type)
                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
            else:  # If the next token is not an identifier token
                # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
                raise syntax_error_except(Self.pace, "Add you variable name")

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

            # While the next token is a ',' symbol token and the subroute keyword is a subroute keyword
            while Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is ',':
                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

            # If the next token is a keyword token and the keyword is a keyword token and the subroute keyword is a subroute keyword
            if Self.Token.Tok_type() is Tok_type.key and Self.Default(Self.Token.key().Val):
                # Save the type of the subroute from the tokenizer object from Tokens.Tokenizer.py file to the Value variable
                Value = Self.Token.key().Val
                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
            elif Self.Token.Tok_type() is Tok_type.id:  # If the next token is an identifier token then
                # Save the type of the subroute from the tokenizer object from Tokens.Tokenizer.py file to the Value variable
                Value = Self.Token.id()
                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
            else:  # If the next token is not a keyword token or the subroute keyword is not a subroute keyword
                # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
                raise syntax_error_except(
                    Self.pace, "Value is not a keyword or identifier")

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

            if Self.Token.Tok_type() is Tok_type.id:  # If the next token is an identifier token then
                # Save the name of the variable from the tokenizer object from Tokens.Tokenizer.py file to the Name variable
                Self.Define_Variable(Self.Token.id(), Value, type)
                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
            else:  # If the next token is not an identifier token
                # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
                raise syntax_error_except(Self.pace, "Add you variable name")

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

    # Compilation Subroute Body function from Compile_Engine.py file
    def Compilation_SubrouteBody(Self):
        Self.Token.Adv()  # Advance the tokenizer object to the next token of the program
        # If the next token is a '{' symbol token and the subroute keyword is a subroute keyword
        if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is '{':
            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
        # If the next token is not a '{' symbol token and the subroute keyword is a subroute keyword
        else:
            # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
            raise syntax_error_except(Self.pace, "{")

        Self.Token.Adv()  # Advance the tokenizer object to the next token of the program
        Self.Local_Var_Count = 0  # Set the local variable count to 0

        # While the next token is a keyword token and the keyword is a keyword token and the subroute keyword is a subroute keyword
        while Self.Token.Tok_type() is Tok_type.key and Self.Token.key() is key.Variable:
            Self.Var_Decl()  # Call the Variable Declaration function from Compile_Engine.py file

        # Write the function name and the local variable count to the VM file
        Self.VM_Writ.Write_Funct(
            Self.Name + "." + Self.Subroute_Name, Self.Local_Var_Count)

        # If the subroute type is a constructor then write the constructor name to the VM file
        if Self.Subroute_Type if key.Constructor:
            # Get the number of fields from the symbol table object from Symbol_Table.py file
            Fields_Count = Self.sym_tab.__Variable_Count__(var_type.Field)
            # Write the PUSH command to the VM file with the number of fields - 1
            Self.VM_Writ.Write_PUSH(Seg.Constructor, Fields_Count - 1)
            # Write the CALL command to the VM file with the memory management system function name and the number of arguments
            Self.VM_Writ.Write_CALL(Constant.Memory_Management_System, 2)
            # Write the POP command to the VM file with the pointer segment and the 0 index
            Self.VM_Writ.Write_POP(Seg.Pointer, 0)

        # If the subroute type is a method then write the method name to the VM file
        elif Self.Subroute_Type if key.Method:
            # Write the PUSH command to the VM file with the argument segment and the 0 index
            Self.VM_Writ.Write_PUSH(Seg.argument, 0)
            # Write the POP command to the VM file with the pointer segment and the 0 index
            Self.VM_Writ.Write_POP(Seg.pointer, 0)

        # Call the Statements Compile function from Compile_Engine.py file
        Self.Statements_Compile()

        # If the next token is a '}' symbol token and the subroute keyword is a subroute keyword
        if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is '}':
            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program
        else:
            # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
            raise syntax_error_except(Self.pace, "}")

    # Compilation Statements function from Compile_Engine.py file
    def Var_Decl(Self):
        # If the next token is a keyword token and the keyword is a keyword token and the subroute keyword is a subroute keyword
        if Self.Token.Tok_type() is Tok_type.key and Self.Token.key() is key.Variable:
            # Set the type of the variable to variable from the var_type.py file
            Type = var_type.Variable
            # Increase the pace of the program by 1 to move to the next token in the source code file
            Self.pace += 1

            # Set the value of the variable to variable from the var_type.py file
            Value = var_type.Variable
            type = empty  # Set the type of the variable to empty from the var_type.py file

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

        else:  # If the next token is not a keyword token and the subroute keyword is a subroute keyword
            return  # If the next token is not a keyword token or the subroute keyword is not a subroute keyword

        # If the next token is a keyword token and the keyword is a keyword token and the subroute keyword is a subroute keyword
        if Self.Token.Tok_type() is Tok_type.key and Self.Default(Self.Token.key().val):
            # Set the type of the variable to the keyword from the Tokens.Tokenizer.py file
            type = Self.Token.key().val
            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
        elif Self.Token.Tok_type() is Tok_type.id:  # If the next token is an identifier token then
            # Set the type of the variable to the identifier from the Tokens.Tokenizer.py file
            type = Self.Token.id()
            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
        else:  # If the next token is not a keyword token or an identifier token then
            # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
            raise syntax_error_except(Self.pace, "Type")

        Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

        if Self.Token.Tok_type() is Tok_type.id:
            # Call the define variable function from Compile_Engine.py file
            Self.define__var(Self.Token.id(), Type, Value)
            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
        else:  # If the next token is not an identifier token then
            # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
            raise syntax_error_except(Self.pace, "Name")

        Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

        # While the next token is a ',' symbol token and the subroute keyword is a subroute keyword
        while Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is ',':
            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

            if Self.Token.Tok_type() is Tok_type.id:  # If the next token is an identifier token then
                # Call the define variable function from Compile_Engine.py file
                Self.define__var(Self.Token.id(), Type, Value)
                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
            else:  # If the next token is not an identifier token then
                # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
                raise syntax_error_except(Self.pace, "Variable Name")

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

        # If the next token is a ';' symbol token and the subroute keyword is a subroute keyword
        if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is ';':
            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program
        else:  # If the next token is not a ';' symbol token and the subroute keyword is a subroute keyword
            # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
            raise syntax_error_except(Self.pace, ";")

    # Compilation Statements function from Compile_Engine.py file
    def statement_compilation(Self):
        # Set the stat_key to the list of the keywords that can be used in a statement
        stat_key = (key.Let, key.If, key.While, key.Return, key.Do)

        # While the next token is a keyword token and the keyword is a keyword token and the subroute keyword is a subroute keyword
        while Self.Token.Tok_type() is Tok_type.key and Self.Token.key().val in stat_key:
            if Self.Token.key().val not in stat_key:  # If the next token is not a keyword token then
                return  # If the next token is not a keyword token or the subroute keyword is not a subroute keyword

            if Self.Token.key().val in stat_key:  # If the next token is a keyword token and the keyword is a keyword token and the subroute keyword is a subroute keyword
                if Self.Token.key().val is key.Let:  # If the next token is a keyword token and the keyword is a keyword token and the subroute keyword is a subroute keyword
                    Self.let_compilation()  # Call the let_compilation function from Compile_Engine.py file
                    Self.Token.Adv()   # Advance the tokenizer object to the next token of the program
                elif Self.Token.key().val is key.If:  # If the next token is a keyword token and the keyword is a keyword token and the subroute keyword is a subroute keyword
                    Self.if_compilation()  # Call the if_compilation function from Compile_Engine.py file
                    Self.Token.Adv()  # Advance the tokenizer object to the next token of the program
                elif Self.Token.key().val is key.While:  # If the next token is a keyword token and the keyword is a keyword token and the subroute keyword is a subroute keyword
                    # Call the while_compilation function from Compile_Engine.py file
                    Self.while_compilation()
                    Self.Token.Adv()  # Advance the tokenizer object to the next token of the program
                elif Self.Token.key().val is key.Return:  # If the next token is a keyword token and the keyword is a keyword token and the subroute keyword is a subroute keyword
                    # Call the return_compilation function from Compile_Engine.py file
                    Self.return_compilation()
                    Self.Token.Adv()  # Advance the tokenizer object to the next token of the program
                elif Self.Token.key().val is key.Do:  # If the next token is a keyword token and the keyword is a keyword token and the subroute keyword is a subroute keyword
                    Self.do_compilation()  # Call the do_compilation function from Compile_Engine.py file
                    Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

    def let_compilation(Self):
        # If the next token is a keyword token and the keyword is a keyword token and the subroute keyword is a subroute keyword
        if Self.Token.Tok_type() is Tok_type.key and Self.Token.key() is key.Let:
            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
        else:  # If the next token is not a keyword token then
            # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
            raise syntax_error_except(Self.pace, "Let")

        Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

        Ind_Assign = False  # Set the Ind_Assign variable to False
        # If the next token is a keyword token and the keyword is a keyword token and the subroute keyword is a subroute keyword
        if Self.Token.Tok_type() is Tok_type.id:
            # Call the var function from Compile_Engine.py file
            var = Self.var(Self.Token.id())

            # Set the value variable to the value of the variable
            value = var[2]
            Ind = var[1]  # Set the Index variable to the index of the variable

            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
        else:  # If the next token is not a keyword token then
            # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
            raise syntax_error_except(Self.pace, "Variable Name")

        Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

        # If the next token is a symbol token and the symbol is a symbol token and the subroute keyword is a subroute keyword
        if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is '[':
            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program
            # Call the Expression_compilation function from Compile_Engine.py file
            Self.Expression_compilation()

            # If the next token is a symbol token and the symbol is a symbol token and the subroute keyword is a subroute keyword
            if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is ']':
                Ind_Assign = True  # Set the Ind_Assign variable to True

                # Write the PUSH command to the VM file
                Self.VM_Writ.Write_PUSH(Seg(value), Ind)
                # Write the ADD command to the VM file to add the value of the variable to the value of the expression
                Self.VM_Writ.Write_Arith(command.Add)

                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
                Self.Token.Adv()  # Advance the tokenizer object to the next token of the program
            else:  # If the next token is not a symbol token then
                # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
                raise syntax_error_except(Self.pace, "]")

            if value:  # If the value variable is not empty then
                # If the variable is an array and the index is not assigned then
                if var[1] == Constant.array_type and not Ind_Assign:
                    # Write the POP command to the VM file
                    Self.VM_Writ.Write_POP(Seg.temp, 0)
                    # Write the POP command to the VM file
                    Self.VM_Writ.Write_POP(Seg.pointer, 1)
                    # Write the PUSH command to the VM file
                    Self.VM_Writ.Write_PUSH(Seg.temp, 0)
                    # Write the POP command to the VM file
                    Self.VM_Writ.Write_POP(Seg.that, 0)
                else:  # If the variable is not an array or the index is assigned then
                    if value is var_type.Field:  # If the value variable is a field variable then
                        # Write the POP command to the VM file
                        Self.VM_Writ.Write_POP(Seg.this, Ind)
                    else:  # If the value variable is not a field variable then
                        # Write the POP command to the VM file
                        Self.VM_Writ.Write_POP(Seg(value), Ind)
            # If the next token is a symbol token and the symbol is a symbol token and the subroute keyword is a subroute keyword
            if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is ';':
                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
            else:  # If the next token is not a symbol token then
                # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
                raise syntax_error_except(Self.pace, ";")

    def if_compilation(Self):
        # If the next token is a keyword token and the keyword is a keyword token and the subroute keyword is a subroute keyword
        if Self.Token.Tok_type() is Tok_type.key and Self.Token.key() is key.If:
            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
        else:  # If the next token is not a keyword token then
            # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
            raise syntax_error_except(Self.pace, "If")

        Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

        # Set the num_line variable to the line number of the token that caused the error
        num_line = string(Self.pace)

        if true_label == "if_true" + num_line:  # If the true_label variable is equal to the IF_TRUE keyword plus the line number of the token that caused the error
            if instead == "if_false" + num_line:  # If the instead variable is equal to the IF_FALSE keyword plus the line number of the token that caused the error
                if end_label == "if_end" + num_line:  # If the end_label variable is equal to the IF_END keyword plus the line number of the token that caused the error

                    # If the next token is a symbol token and the symbol is a symbol token and the subroute keyword is a subroute keyword
                    if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is '(':
                        Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

                        Self.Token.Adv()  # Advance the tokenizer object to the next token of the program
                        Self.expression_compilation()

                        # Write the IF command to the VM file with the true_label variable
                        Self.VM_Writ.Write_If(true_label)
                        # Write the GOTO command to the VM file with the instead variable to go to the else statement
                        Self.VM_Writ.Write_Goto(instead)
                        # Write the label command to the VM file with the end_label variable to go to the end of the if statement
                        Self.VM_Writ.Write_Label(end_label)

                        # If the next token is a symbol token and the symbol is a symbol token and the subroute keyword is a subroute keyword
                        if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is ')':
                            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
                        else:  # If the next token is not a symbol token then
                            # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
                            raise syntax_error_except(Self.pace, ")")

                        Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

                        # If the next token is a symbol token and the symbol is a symbol token and the subroute keyword is a subroute keyword
                        if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is '{':
                            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
                            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

                            # Write the label command to the VM file with the true_label variable
                            Self.VM_Writ.Write_Label(true_label)
                            Self.statement_compilation()  # Compile the statement of the if statement

                            # If the next token is a symbol token and the symbol is a symbol token and the subroute keyword is a subroute keyword
                            if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is '}':
                                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
                            else:
                                # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
                                raise syntax_error_except(Self.pace, "}")

                            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

                            if Self.Token.Tok_type() is Tok_type.key and Self.Token.key() is key.Else:
                                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

                                Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

                                # Write the GOTO command to the VM file with the end_label variable to go to the end of the if statement
                                Self.VM_Writ.Write_Goto(end_label)

                            # If the next token is a symbol token and the symbol is a symbol token and the subroute keyword is a subroute keyword
                            if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is '{':
                                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

                                Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

                                # Write the label command to the VM file with the instead variable to go to the else statement
                                Self.VM_Writ.Write_Label(instead)
                                Self.statement_compilation()  # Compile the statement of the else statement

                                Self.VM_Writ.Write_Label(end_label)
                                # If the next token is a symbol token and the symbol is a symbol token and the subroute keyword is a subroute keyword
                                if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is '}':
                                    Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
                                else:  # If the next token is not a symbol token then
                                    # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
                                    raise syntax_error_except(Self.pace, "}")
                            else:  # If the next token is not a symbol token then
                                # Write the label command to the VM file with the instead variable to go to the else statement
                                Self.VM_Writ.Write_Label(instead)
                                return  # Return to the previous function call

        # Compile the return statement of the program
        def __return_compilation__(Self):
            # If the next token is a keyword token and the keyword is a return keyword then
            if Self.Token.Tok_type() is Tok_type.key and Self.Token.key() is key.Return:
                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
            else:  # If the next token is not a keyword token then
                # Raise a syntax error exception and print the line number of the token that caused the error and the token that caused the error in the source code file
                raise syntax_error_except(Self.pace, "Return")

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

            # If the next token is a symbol token and the symbol is a symbol token and the subroute keyword is a subroute keyword
            if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is ';':
                # Write the push command to the VM file with the constant segment and the value of 0 to push the value of 0 to the stack
                Self.VM_Writ.Write_Push(Segment.const, 0)
                Self.Token.Adv()  # Advance the tokenizer object to the next token of the program
            else:  # If the next token is not a symbol token then
                Self.expression_compilation()  # Compile the expression of the return statement

            # If the next token is a symbol token and the symbol is a symbol token and the subroute keyword is a subroute keyword
            if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is ';':
                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
            else:  # If the next token is not a symbol token then
                # Raise a syntax error exception and print the line number of the token that caused
                # the error and the token that caused the error in the source code file
                raise syntax_error_except(Self.pace, ";")

            # Write the return command to the VM file to return the value of the stack to the caller of the function
            Self.VM_Writ.Write_Return()

    def expression_compilation(Self):  # Compile the expression of the program
        # List of the operators of the expression
        Ops = ['+', '-', '*', '/', '&', '|', '<', '>', '=']
        Self.term_compilation()  # Compile the term of the expression
        if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() in Ops:
            Ops = Self.Token.sym()  # Set the operator to the symbol of the token

            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

            if Ops is '*':
                # Write the call command to the VM file to call the multiply function with 2 arguments
                Self.VM_Writ.Write_Call('Math.multiply', 2)
            elif Ops is '/':
                # Write the call command to the VM file to call the divide function with 2 arguments
                Self.VM_Writ.Write_Call('Math.divide', 2)
            else:
                # Write the arithmetic command to the VM file with the operator to perform the operation
                Self.VM_Writ.Write_Arithmetic(command(Ops))

    def term_compilation(Self):  # Compile the term of the expression
        single_ops = ['-', '~']
        key_Constants = ["False", "True", "null", "this"]
        # If the next token is a symbol token and the symbol is a symbol token and the subroute keyword is a subroute keyword
        if Self.Token.Tok_type() is Tok_type.str_Constant:
            # Set the string value to the string value of the token
            Str_Val = Self.Token.Str_Val()
            # Set the dimension of the string to the length of the string value
            dim = len(Str_Val)
            # Set the characters of the string to the characters of the string value
            characters = [word for word in Str_Val]

            # Write the push command to the VM file with the constant segment and the value of the dimension of the string
            # to push the value of the dimension of the string to the stack
            Self.VM_Writ.Write_Push(Seg.const, dim)
            # Write the call command to the VM file to call the new string function with 1 argument
            Self.VM_Writ.Write_Call(Constant.String.new, 1)

            for char in characters:  # For each character in the characters of the string value
                # Write the push command to the VM file with the constant segment and the value of the ASCII value of the character
                # to push the value of the ASCII value of the character to the stack
                Self.VM_Writ.Write_Push(Seg.const, ord(char))
                # Write the call command to the VM file to call the append char function with 2 arguments
                Self.VM_Writ.Write_Call(Constant.String.appendChar, 2)

            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

        elif Self.Token.Tok_type() is Tok_type.num_Constant:  # If the next token is a number token then
            # Write the push command to the VM file with the constant segment and the value of the value to push the value of the value to the stack
            Self.VM_Writ.Write_Push(Seg.const, Self.Token.num_Val())
            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

        # If the next token is a keyword token and the keyword is a constant keyword
        elif Self.Token.Tok_type() is Tok_type.key and Self.Token.key().value in key_Constants:
            if Self.Token.key().val == "null" or Self.Token.key().val == "false":
                # Write the push command to the VM file with the constant segment and the value of 0 to push the value of 0 to the stack
                Self.VM_Writ.Write_Push(Seg.const, 0)
            elif Self.Token.key().val == "true":  # If the next token is a keyword token and the keyword is a constant keyword
                # Write the push command to the VM file with the constant segment and the value of 1 to push the value of 1 to the stack
                Self.VM_Writ.Write_Push(Seg.const, 1)
                # Write the arithmetic command to the VM file with the operator to perform the operation
                Self.VM_Writ.Write_Arithmetic(command.Neg)
            elif Self.Token.key().val == "this":  # If the next token is a keyword token and the keyword is a constant keyword
                # Write the push command to the VM file with the pointer segment and the value of 0 to push the value of 0 to the stack
                Self.VM_Writ.Write_Push(Seg.pointer, 0)
            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

        # If the next token is a symbol token and the symbol is a symbol token and the subroute keyword is a subroute keyword
        elif Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() == '(':
            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program
            # Compile the expression of the program in the parenthesis
            Self.expression_compilation()

            if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() == ')':
                Self.pace += 1

                Self.Token.Adv()  # Advance the tokenizer object to the next token of the program
            else:
                # Raise a syntax error exception and print the line number of the token that caused
                # the error and the token that caused the error in the source code file
                raise syntax_error_except(Self.pace, ")")

        elif Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() in single_ops:
            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
            Ops = Self.Token.sym()  # Set the operator to the symbol of the token

            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

            # Compile the term of the expression in the parenthesis
            Self.term_compilation()

            if Ops is '-':  # If the operator is a minus operator then
                # Write the arithmetic command to the VM file with the operator to perform the operation
                Self.VM_Writ.Write_Arithmetic(command.Neg)
            elif Ops is '~':  # If the operator is a bitwise not operator then
                # Write the arithmetic command to the VM file with the operator to perform the operation
                Self.VM_Writ.Write_Arithmetic(command.Not)

        elif Self.Token.Tok_type() is Tok_type.id:
            Name = Self.Token.id()  # Set the name to the identifier of the token
            # Get the variable from the symbol table with the name of the identifier
            Var = Self.Get_Var(Name)
            Sub_Name = " "  # Set the subroute to an empty string
            ref_method = False  # Set the reference method to false

            if Var:  # If the variable is not None
                # Get the segment of the variable from the symbol table
                Seg = Self.Get_Seg(Var[2])

                if Seg is Seg.this:  # If the segment is the this segment then
                    # Set the subroute to the name of the variable plus a period to access the variable
                    Sub_Name = Var[1] + "."
                    ref_method = True  # Set the reference method to true if the variable is a method
                # Write the push command to the VM file with the segment and the value of the variable
                Self.VM_Writ.Write_Push(Seg, Var[3])
            else:  # If the variable is None
                # Set the subroute to the name of the variable plus a period to access the variable
                Sub_Name = Name + "."

                Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

                # If the next token is a symbol token and the symbol is a symbol token and the symbol is a period
                if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() == "(" or Self.Token.Tok_type() == ".":
                    # If the next token is a symbol token and the symbol is a symbol token and the symbol is a period
                    if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() == "(":
                        Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

                        Self.expression_compilation()
                        if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() == ")":
                            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
                        else:
                            # Raise a syntax error exception and print the line number of the token that caused
                            # the error and the token that caused the error in the source code file
                            raise syntax_error_except(Self.pace, ")")
                    elif Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() == ".":
                        Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

                        Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

                        if Self.Token.Tok_type() is Tok_type.id:
                            # Set the subroute to the subroute plus the name of the token
                            Sub_Name += Self.Token.id()
                            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
                        else:
                            # Raise a syntax error exception and print the line number of the token that caused
                            # the error and the token that caused the error in the source code file
                            raise syntax_error_except(
                                Self.pace, "subroute name")

                        Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

                        if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is "(":
                            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

                            Self.expression_compilation()

                            if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is ")":
                                Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

                            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program
                        else:
                            # Raise a syntax error exception and print the line number of the token that caused
                            # the error and the token that caused the error in the source code file
                            raise syntax_error_except(Self.pace, ")")

                    # If the subroute is not a method then
                    if ref_method:
                        Self.Para_Count += 1  # Set the parameter count to 1 more than the previous parameter count
                        # Write the call command to the VM file with the subroute and the parameter count
                        Self.VM_Writ.Write_Call(Sub_Name, Self.Para_Count)
                    # If the subroute is a method then and the next token is a symbol token and the symbol is a symbol token and the symbol is a square bracket
                    elif Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is "[":
                        Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

                        # Compile the expression of the program in the parenthesis
                        Self.expression_compilation()
                        Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

                        # Write the call command to the VM file with the subroute and the parameter count
                        Self.VM_Writ.Write_Call(Sub_Name, Self.Para_Count)

                # If the next token is a symbol token and the symbol is a symbol token and the symbol is a square bracket
                elif Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is "[":
                    Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file
                    # Compile the expression of the program in the parenthesis
                    Self.expression_compilation()
                    Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

                    Self.VM_Writ.Write_Arith(command.Add)
                    Self.VM_Writ.Write_Pop(Seg.pointer, 1)
                    Self.VM_Writ.Write_Push(Seg.that, 0)

                    if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is "]":
                        Self.pace += 1

                        Self.Token.Adv()  # Advance the tokenizer object to the next token of the program
                    else:
                        # Raise a syntax error exception and print the line number of the token that caused
                        # the error and the token that caused the error in the source code file
                        raise syntax_error_except(Self.pace, "]")

    # Compile the expression of the program in the parenthesis
    def expression_compilation(Self):
        Self.Para_Count = 0  # Set the parameter count to 0

        Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

        # If the next token is a symbol token and the symbol is a symbol token and the symbol is a parenthesis
        if Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is ")":
            return  # Return from the function if the next token is a symbol token and the symbol is a symbol token and the symbol is a parenthesis

        Self.expression_compilation()  # Compile the expression of the program
        Self.Para_Count += 1  # Increase the parameter count by 1

        if Self.Token.Tok_type() is not Tok_type.sym:
            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

        while Self.Token.Tok_type() is Tok_type.sym and Self.Token.sym() is ",":
            Self.pace += 1  # Increase the pace of the program by 1 to move to the next token in the source code file

            Self.expression_compilation()  # Compile the expression of the program
            Self.Para_Count += 1  # Increase the parameter count by 1
            Self.Token.Adv()  # Advance the tokenizer object to the next token of the program

    # Default method for the tokenizer object to call if the token is not a keyword
    def Default(Self, Token):
        # Return true if the token is a keyword and false if it is not
        return Token in ["char", "int", "boolean"]

    def variable(Self, key):  # Method to check if the token is a variable
        # Return true if the token is a variable and false if it is not
        return key.static or key is key.field

    def subroute(Self, key):  # Method to check if the token is a subroute or a method
        # Return true if the token is a subroute or a method and false if it is not
        return Self.Token.key() is key.constructor or Self.Token.key() is key.function or Self.Token.key() is key.method

    def Defined(Self, Name):  # Method to check if the token is a defined variable
        # Return true if the token is a defined variable and false if it is not
        return Name in Self.Sym_Tab.Ind(Name)

    def def_var_(Self, Name, Type, Val):  # Method to define a variable in the symbol table
        # Get the index of the variable in the symbol table if it is already defined
        Ind = Self.var__def(Name)

        if Ind is None:  # If the variable is not defined then
            # Get the index of the variable in the symbol table
            Ind = Self.Sym_Tab.var_count(Val)
            # Add the variable to the symbol table with the type, value, and name
            Self.Sym_Tab.var_count(Type, Val, Name)
        else:  # If the variable is already defined then raise a syntax error exception
            if Ind.type is not Type:  # If the type of the variable is not the same as the type of the variable then
                # Raise a syntax error exception and print the line number of the token that caused
                raise syntax_error_except(Self.pace, "variable type")
            if Ind.val is not Val:  # If the value of the variable is not the same as the value of the variable then
                # Raise a syntax error exception and print the line number of the token that caused
                raise syntax_error_except(Self.pace, "variable value")

    def Get__var(Self, Name):  # Method to get the index of a variable in the symbol table
        # Get the index of the variable in the symbol table
        Ind = Self.var__def(Name)

        if Ind > 0:  # If the variable is defined then
            # Get the value of the variable in the symbol table
            Val = Self.Sym_Tab.Val(Name)
            # Get the index of the variable in the symbol table
            Ind = Self.Sym_Tab.Ind(Name)
            # Get the type of the variable in the symbol table
            Type = Self.Sym_Tab.Type(Name)
            # Return the type, value, index, and name of the variable
            return (Type, Val, Ind, Name)
        else:  # If the variable is not defined then raise a syntax error exception
            return None

    def Get__Seg(Self, Val):  # Method to get the segment of a variable in the symbol table
        if Val is var_type.Field:  # If the value is a field then return the field segment
            return Seg.this  # Return the field segment of the variable
        else:  # If the value is not a field then return the static segment of the variable
            return Seg(Val)  # Return the static segment of the variable
