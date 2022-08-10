################################################################################################
"""
    Name: Mangesh Bhattacharya 
    Course: Computer Fundamentals
    Code: DCN 250
    Inst: Dr. Yousef Ashibani
"""
################################################################################################

# for creating namedtuple objects for the tokens and the lexer
from collections import namedtuple

from numpy import empty  # for creating empty arrays for the tokens

# symbol object to store value and balance of a variable in the VM code file
jk_sym = namedtuple("jk_sym", "value id")


class jk_class:  # class object for class declaration in Jack code

    def __init__(Self, Name):  # Constructor for jk_class class to create a class object with name
        Self.Name = Name  # Name of class to be created in the VM code file
        # symbol table for class object (local, argument, static, this, that, pointer, temp)
        Self.sym = dict()

    # add field variable to symbol table for class object with name and type (this, that, pointer, temp)
    def Field(Self, Name, variable_type):
        # add symbol to symbol table for class object with value and balance (this, that, pointer, temp)
        Self.sym[Name] = jk_sym(variable_type, "Field")
        Self.Field_sym += 1  # increment field symbol count for class object with name and type

    # add static variable to symbol table for class object with name and type
    def Static(Self, Name, variable_type):
        # add symbol to symbol table for class object with value and balance
        Self.sym[Name] = jk_sym(variable_type, "Static")
        Self.Static_sym += 1  # increment static symbol count for class object

    def sym(Self, Name):  # get symbol from symbol table for class object
        # get value from symbol object (local, argument, static, this, that, pointer, temp)
        return Self.sym.__get__[Name]


# class object for subroutine declaration in Jack code (method, function)
class jk_sub:

    # Constructor for jk_sub class to create a subroutine object with name, subroutine type, return type, and class object
    def __init__(Self, Name, sub_type, ret_type, jk_cls):
        Self.Name = Name  # Name of subroutine to be created in the VM code file
        # subroutine type (constructor, function, method)
        Self.sub_type = sub_type
        Self.ret_type = ret_type  # return type of subroutine to be created in the VM code file
        Self.jk_cls = jk_cls  # class object of subroutine

        # symbol table for subroutine object (local, argument, static, this, that, pointer, temp)
        Self.sym = dict()
        Self.Arg_sym = 0  # argument symbol count for subroutine object
        Self.variable_sym = 0  # variable symbol count for subroutine object

        if sub_type == "method":  # if subroutine type is method add this to symbol table for subroutine object
            # add this to symbol table for subroutine object with name and type (this, that, pointer, temp)
            Self.Arg_sym(Self.jk_cls.Name, "This")

    # add argument variable to symbol table for subroutine object with name and type
    def Argument(Self, Name, variable_type):
        # add symbol to symbol table for subroutine object with value and balance
        Self.sym[Name] == jk_sym["argument", variable_type, Self.Arg_sym]
        Self.Arg_sym += 1  # increment argument symbol count for subroutine object

    # add variable to symbol table for subroutine object
    def variable(Self, Name, variable_type):
        # add symbol to symbol table for subroutine object
        Self.sym[Name] == jk_sym["variable", variable_type, Self.variable_sym]
        Self.variable_sym += 1  # increment variable symbol count for subroutine object

    def sym_get(Self, Name):  # get symbol from symbol table for subroutine object (local, argument, static, this, that, pointer, temp)
        # get symbol from symbol table for subroutine object with name
        Sym = Self.sym.Get(Name)
        if Sym is not empty:  # if symbol is not empty return symbol
            return Sym  # return symbol object from symbol table for subroutine object

        # if symbol is empty return symbol from symbol table for class object
        return Self.jk_cls.Sym_Get(Name)
