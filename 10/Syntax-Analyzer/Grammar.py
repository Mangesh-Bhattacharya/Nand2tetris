################################################################################################
"""
    Name: Mangesh Bhattacharya 
    Course: Computer Fundamentals
    Code: DCN 250
    Inst: Dr. Yousef Ashibani
"""
################################################################################################
#####
# Grammar Consructor
#####

import re  # Regular Expressions


class grammar:  # Grammar Constructor

    Symbol_Mappings = {  # Symbol Mappings for Grammar
        '\"': "&quot;",  # Quotation Mark
        "&": "&amp;",  # Ampersand Symbol
        "<": "&lt;",  # Less Than Symbol
        ">": "&gt;",  # Greater Than
    }   # Symbol_Mappings

    def key(Token):  # Static Method to check if Token is a Key
        key = ["class",  # Class Keyword
               "constructor",  # Constructor Keyword
               "function",  # Function Keyword
               "method",  # Method Keyword
               "field",  # Field Keyword
               "static",  # Static Keyword
               "variable",  # Variable Keyword
               "integer",  # Integer Keyword
               "character",  # Character Keyword
               "string",  # String Keyword
               "array",  # Array Keyword
               "boolean",  # Boolean Keyword
               "void",  # Void Keyword
               "true",  # True Keyword
               "false",  # False Keyword
               "null",  # Null Keyword
               "this",  # This Keyword
               "let",  # Let Keyword
               "do",  # Do Keyword
               "if",  # If Keyword
               "else",  # Else Keyword
               "while",  # While Keyword
               "return"  # Return Keyword
               ]  # Keywords List
        return Token in key  # Return True if Token is a Keyword

    def symbol(Token):  # Static Method to check if Token is a Symbol
        sym = ["{",
               "}",
               "(",
               ")",
               "[",  # Array Index
               "]",  # Array Symbol
               ".",  # Separates Class Name from Variable Name
               ",",  # Comma Symbol
               ";",  # Separator Symbol
               "+",  # Addition Operator
               "-",  # Subtraction Operator
               "*",  # Multiplication Operator
               "/",  # Division Operator
               "&",  # Ampersand Symbol
               "|",  # Bitwise OR
               "<",  # Less Than Symbol
               ">",  # Greater Than
               "=",  # Equal Symbol
               "~"  # Negation Symbol
               ]    # Symbol List
        return Token in sym  # Return True if Token is a Symbol

    def id(Token):  # Static Method to check if Token is an Identifier
        # Return True if Token is an Identifier
        return Token.begins_with("\"") and Token.ends_with("\"")

    def int(Token):  # Static Method to check if Token is an Integer Value
        try:  # Try to convert Token to an Integer and return True if successful else return False
            # Try to convert Token to an Integer and return True if successful
            int = int(Token)
            # Return True if Token is an Integer between 0 and 32767
            return int >= 0 and int <= 32767
        except ValueError:  # Return False if Token is not an Integer between 0 and 32767
            return False  # Return False if Token is not an Integer between 0 and 32767 or if Token is not an Integer

    def str(Token):  # Static Method to check if Token is a String Value
        # Return True if Token is a String Value
        return Token.begins_with("\"") and Token.ends_with("\"")

    def mapping_sym(cla, sym):  # Static Method to map Symbols to HTML Symbols for HTML Output File
        if sym in cla.sym_maps:  # If Symbol is in Symbol Mappings Dictionary return Symbol Mapping
            # Return Symbol Mapping if Symbol is in Symbol Mappings Dictionary
            return cla.sym_maps[sym]
        # If Symbol is not in Symbol Mappings, return Symbol as it is (i.e. without any modifications)
        else:
            # Return Symbol as it is (i.e. without any modifications)
            return sym
