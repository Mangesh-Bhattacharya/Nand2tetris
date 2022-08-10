# for enum type checking in the code generator (Segment, Command)
################################################################################################
"""
    Name: Mangesh Bhattacharya 
    Course: Computer Fundamentals
    Code: DCN 250
    Inst: Dr. Yousef Ashibani
"""
################################################################################################

from enum import Enum


class Seg(Enum):  # Segment enum type for the code generator

    Constant = "constant"  # Constant segment name in the code generator
    local = "local"  # Local segment name in the code generator
    argument = "argument"  # Argument segment name in the code generator
    this = "this"  # This segment name in the code generator
    that = "that"  # That segment name in the code generator
    pointer = "pointer"  # Pointer segment name in the code generator
    temp = "temp"  # Temp segment name in the code generator
    static = "static"  # Static segment name in the code generator
