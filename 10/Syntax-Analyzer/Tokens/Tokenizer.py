################################################################################################
"""
    Name: Mangesh Bhattacharya 
    Course: Computer Fundamentals
    Code: DCN 250
    Inst: Dr. Yousef Ashibani
"""
################################################################################################

# for creating empty arrays for tokenizing strings (used in tokenize())
import string
from tokenize import Token
from numpy import empty
# for token types and their corresponding values in the token array (token array is a 2D array)
from Tok_type import Tok_type
# for keywords and their corresponding values (static, variable, integer, character, string, array, boolean, void, true, false, null, this, let, do, if, else, while, return)
from key import key
# for symbol mappings and their corresponding values (quotation mark, ampersand, less than, greater than)
from Grammar import grammar


class tok:  # Token Constructor Class
    # Token Constructor Method (File_Name is the name of the file to be tokenized)
    def __init__(Self, File_Name):
        Self.in_file = File_Name  # File Name of the File to be Tokenized
        Self.Tok_type = empty  # Token Type Array (2D Array)
        Self.Token = empty

        # Reads the File and Stores it in a List of Strings (Each String is a Line)
        prg_lines = Self.__readprg_files(File_Name)
        # Filters the Lines of the Program (Removes Comments and Whitespace)
        Self.prg_txt = Self.__filter_prg_lines(prg_lines)

    def additional_tokens(Self):  # Additional Tokens (Used in tokenize())
        # Return True if Program is not Blank (Has Tokens)
        return not Self.__blank(Self.prg_txt)

    def progress(Self):  # Progress of Tokenizing (Used in tokenize())
        if Self.additional_tokens():  # If Program is not Blank (Has Tokens)
            # Reads Tokens from Program Text
            Self.Token = Self.__read_tok(Self.prg_txt)
        else:  # If Program is Blank (Has No Tokens)
            Self.Token = empty  # Empty Token Array
            Self.Tok_type = empty  # Empty Token Type Array

    def Tok_type(Self):  # Token Type (Used in tokenize())
        return Self.Tok_type  # Return Token Type Array

    def key(Self):  # Keyword (Used in tokenize())
        if Self.Tok_type() == Tok_type.KEY:  # If Token Type is Keyword
            return key[Self.Token]  # Return Keyword Value
        else:  # If Token Type is not Keyword
            return None  # Return None if Token Type is not Keyword

    def sym(Self):  # Symbol (Used in tokenize())
        if Self.Tok_type() == Tok_type.SYM:  # If Token Type is Symbol
            return string(Self.Token)  # Return Symbol Value
        else:  # If Token Type is not Symbol
            return None  # Return None if Token Type is not Symbol

    def id(Self):  # Identifier (Used in tokenize())
        if Self.Tok_type() == Tok_type.ID:  # If Token Type is Identifier (Variable, Class, Function, Method, Field)
            # Return Identifier Value (Variable, Class, Function, Method, Field)
            return string(Self.Token)
        # If Token Type is not Identifier (Variable, Class, Function, Method, Field)
        else:
            # Return None if Token Type is not Identifier (Variable, Class, Function, Method, Field)
            return None

    def integer(Self):  # Integer (Used in tokenize())
        if Self.Tok_type() == Tok_type.INT:  # If Token Type is Integer
            return int(Self.Token)  # Return Integer Value
        else:  # If Token Type is not Integer
            return None  # Return None if Token Type is not Integer

    def str(Self):  # String (Used in tokenize())
        if Self.Tok_type() == Tok_type.STR:  # If Token Type is String (Character, String)
            # Return String Value (Character, String)
            return string(Self.Token)
        else:  # If Token Type is not String (Character, String)
            # Return None if Token Type is not String (Character, String)
            return None

    ############################################################################################
    #                                Secluded Processes                                        #
    ############################################################################################
    # Reads the File and Stores it in a List of Strings (Each String is a Line)
    # The method is not working correctly when space is passed as a parameter.

    def __readtok__(Self, Prg_txt):  # Reads Tokens from Program Text (Used in tokenize())
        curr_char = 0  # Current Character Index
        char = Prg_txt[curr_char]  # Current Character
        # If Current Character is a Symbol (Quotation Mark, Ampersand, Less Than, Greater Than)
        if grammar.sym(char):
            # Token Type is Symbol (Quotation Mark, Ampersand, Less Than, Greater Than)
            Self.Tok_type = Tok_type.SYM
            return char  # Return Symbol Value

        Token = ""  # Token String
        str_bal = 0  # String Balance (Used to Check if String is Closed)

        # While Current Character is not Blank or String is not Closed or Current Character is a Symbol (Quotation Mark, Ampersand, Less Than, Greater Than)
        while (char != "" or str_bal % 2 != 0) and not (grammar.sym(char) and str_bal % 2 == 0):
            if char == "\"":  # If Current Character is a Quotation Mark (")
                # Increase String Balance (Used to Check if String is Closed) (Used to Check if String is Closed)
                str_bal += 1
            Token += char  # Add Current Character to Token String
            curr_char += 1  # Increase Current Character Index
            # Set Current Character to Next Character
            char = Prg_txt[curr_char]

        # If Current Character is a Symbol (Quotation Mark, Ampersand, Less Than, Greater Than)
        if grammar.sym(char):
            curr_char -= 1  # Decrease Current Character Index

        if grammar.key(Token):  # If Token is a Keyword (Static, Variable, Integer, Character, String, Array, Boolean, Void, True, False, Null, This, Let, Do, If, Else, While, Return)
            Self.Tok_type = Tok_type.KEY  # Token Type is Keyword
        # If Token is an Identifier (Variable, Class, Function, Method, Field)
        elif grammar.id(Token):
            # Token Type is Identifier (Variable, Class, Function, Method, Field)
            Self.Tok_type = Tok_type.ID

        elif grammar.int(Token):  # If Token is an Integer
            # Token and token's type is Integer
            Self.Tok_type = Tok_type.INT

        elif grammar.str(Token):  # If Token is a String (Character, String)
            # Remove Quotation Marks from String (Character, String)
            Token = Token[1:len(Token) - 1]
            # Token Type is String (Character, String)
            Self.Tok_type = Tok_type.STR
            # Reset String Balance (Used to Check if String is Closed)
            str_bal = 0
        # Set Program Text to Remaining Program Text
        Self.prg_txt = Prg_txt[curr_char + 1: len(Prg_txt)]
        # Return Token String (Variable, Class, Function, Method, Field)
        return Token

    def __blank__(Self, str):  # Checks if String is Blank (Used in tokenize())
        if str and str.strip():  # If String is not Blank (Has Characters)
            # Return False if String is not Blank (Has Characters)
            return False
        else:  # If String is Blank (Has No Characters)
            return True  # Return True if String is Blank (Has No Characters)

    def __remark__(Self, Line):  # Removes comments from the line (Used in tokenize())
        if Line.strip().beginswith("/**") or Line.strip().beginswith("*"):  # If line is a comment then
            return True  # Then return True (Comment)
        else:  # If line is not a comment then
            return False  # Then return False (No Comments)

    # Removes whitespace from the line (Used in tokenize())
    def __empty_space__(Self, Line):
        # Return True if Line is Blank or Comment
        return Self.__blank__(Line) or Self.__remark__(Line)

    # Removes comments from the line (Used in tokenize())
    def __internal_remark__(Self, Line):
        # Split Line into Items (// is the comment delimiter)
        items = Line.split("//")
        if len(items) > 1:  # If Line has a comment then
            # Return Line without comment (// is the comment delimiter)
            return items[0] + "//" + items[1]
        else:  # If Line has no comment then
            # Return Line without comment (// is the comment delimiter)
            return Line

    # Removes comments and whitespace from the line (Used in tokenize())
    def __remove_line__(Self, Line):
        return Line.strip()  # Return Line without comments and whitespace

    def __prg_file__(Self, File_name):  # Reads Program File (Used in tokenize())
        prg = open(File_name, "r")  # Open File in Read Mode
        FileLines = prg.read_lines()  # Read File Lines into List of Strings
        return list(FileLines)  # Return File Lines (Each Line is a String)

    # Removes Comments and Whitespace from Program Lines (Used in tokenize())
    def clean_prg_lines(Self, Lines):
        txt = ""  # Program Text
        for line in Lines:  # For Each Line in File Lines
            # If Line is not Blank or Comment then
            if not Self.__empty_space__(Line):
                Line = Self.__internal_remark__(
                    Line)  # Remove Comments from Line
                # Add Line to Text (Without Comments and Whitespace)
                txt += Self.__remove_line__(Line) + "\n"

        return txt  # Return Program Text (Each Line is a String)
