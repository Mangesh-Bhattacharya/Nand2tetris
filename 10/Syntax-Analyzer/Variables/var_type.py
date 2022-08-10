################################################################################################
"""
    Name: Mangesh Bhattacharya 
    Course: Computer Fundamentals
    Code: DCN 250
    Inst: Dr. Yousef Ashibani
"""
################################################################################################

from enum import Enum  # for enum type (Token Type)


class var_type(Enum):   # for enum type (Variable Type)
    Static = "Stat"     # for static variable type
    Variable = "Lcl"    # for local variable type
    Field = "Field"     # for field variable type
    Argument = "Arg"    # for argument variable type
    Class = "cls"       # for class variable type
    subroutine = "subroute"  # for subroutine variable type
