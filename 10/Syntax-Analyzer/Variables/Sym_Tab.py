"""
Mangesh Bhattacharya | 039-251-145
"""
from tkinter import Variable
from Variables.var_type import var_type


class Sym_Tab:  # Symbol Table Class for Variables and Functions

    def __init__(Self):  # Constructor for Symbol Table Class
        Self.class__table__ = {}  # Class Symbol Table
        Self.subroute__table__ = {}  # Subroutine Symbol Table

        def __begin_subroute__(Self):  # Begin Subroutine Method
            Self.subroute__table__ = {}  # Reset Subroutine Symbol Table

        def __Define__(Self, Name, Type, Value):  # Define Method
            if not Self._Get_Name(Name):  # If Name is not already defined
                # Create Variable called Name with Type and Value
                Variables = (Name, Type, Value, Self.Variable_Count(Value))

                # If Value is Static or Field (Class or Subroutine)
                if Value is var_type.Static or Value is var_type.Field:
                    # Add to Class Symbol Table (Static or Field)
                    Self.class__table__[Name] = Variables

    # Variable Count Method for Static or Field Variables
    def __Variable_Count__(Self, Value):
        Variable_Count = 1  # Variable Count is 1 by Default
        if Value is var_type.Static or Value is var_type.Field:  # If Value is Static or Field
            for Variable in Self.class__table__:  # For Each Variable in Class Symbol Table
                # Get Variable from Class Symbol Table as Tuple (Name, Type, Value, Variable_Count)
                Variable = Self.class__table__[Variable]
                # If Variable Value is Value (Static or Field)
                if Variable[2] is Value:
                    Variable_Count += 1  # Increment Variable Count by 1
        elif Value is var_type.Argument or Value is var_type.Variable:  # If Value is Argument or Variable
            # For Each Subroutine in Subroutine Symbol Table (Name, Type, Value, Variable_Count)
            for subroute in Self.subroute__table__:
                # Get Subroutine from Subroutine Symbol Table as Tuple
                subroute = Self.subroute__table__[subroute]
                # If Subroutine Value is Value (Argument or Variable)
                if subroute[2] is Value:
                    # Increment Variable Count by 1 (Argument or Variable)
                    Variable_Count += 1

        return Variable_Count  # Return Variable Count

    def __Value__(Self, Name):  # Value Method for Variable Name
        # Get Variable from Symbol Table as Tuple (Name, Type, Value, Variable_Count)
        Variable = Self._Get_Name(Name)
        if Variable:  # If Variable is Found in Symbol Table
            return Variable[2]  # Return Variable Value
        else:  # If Variable is Not Found in Symbol Table
            return None  # Return Nothing

    def __Type__(Self, Name):  # Type Method for Variable Name
        # Get Variable from Symbol Table as Tuple (Name, Type, Value, Variable_Count)
        Variable = Self._Get_Name(Name)
        if Variable:  # If Variable is Found in Symbol Table
            return Variable[1]  # Return Variable Type of Name
        else:  # If Variable is Not Found in Symbol Table (Name is not defined)
            return None  # Return Nothing

    def __Index__(Self, Name):  # Index Method for Variable Name
        # Get Variable from Symbol Table as Tuple (Name, Type, Value, Variable_Count)
        Variable = Self._Get_Name(Name)
        if Variable:  # If Variable is Found in Symbol Table
            return Variable[3]  # Return Variable Index of Name
        else:  # If Variable is Not Found in Symbol Table (Name is not defined)
            return None  # Return Nothing

    def __Name__(Self, Name):  # Name Method for Variable Name
        if Name in Self.class__table__:  # If Name is in Class Symbol Table
            # Return Name from Class Symbol Table as Tuple (Name, Type, Value, Variable_Count)
            return Self.class__table__[Name]
        elif Name in Self.subroute__table__:  # If Name is in Subroutine Symbol Table
            # Return Name from Subroutine Symbol Table as Tuple
            return Self.subroute__table__[Name]
        else:  # If Name is Not Found in Symbol Table
            return None  # Return Nothing

    def Print(Self):  # Print Method for Symbol Table Class
        print(" \n ")  # Print Blank Line for Readability of Output in Console Window
        # Print Variable Symbol Table Header
        print("Variable Symbol Table:   ")
        print(" \n ")  # Print Blank Line for Readability of Output in Console Window
        for Variable in Self.class__table__:
            # Get Variable from Class Symbol Table as Tuple (Name, Type, Value, Variable_Count)
            Variable = Self.class__table__[Variable]
            # Print Variable from Class Symbol Table
            print("Name: " + Variable[0] + " Type: " + Variable[1] +
                  " Value: " + Variable[2] + " Index:   \n" + str(Variable[3]))
            # Print Blank Line for Readability of Output in Console Window
            print(" \n ")
        # Print Subroutine Symbol Table Header
            print("Subroutine Symbol Table:   ")
            # Print Blank Line for Readability of Output in Console Window
            print(" \n ")
        # For Each Subroutine in Subroutine Symbol Table (Name, Type, Value, Variable_Count)
        for subroute in Self.subroute__table__:
            # Get Subroutine from Subroutine Symbol Table as Tuple
            subroute = Self.subroute__table__[subroute]
            # Print Subroutine from Subroutine Symbol Table
            print("Name: " + subroute[0] + " Type: " + subroute[1] +
                  " Value: " + subroute[2] + " Index:   \n" + str(subroute[3]))  # Print Blank Line for Readability of Output in Console Window. Window for Readability of Output in Console Window in Console Window.
