from enum import Enum  # for enum type checking in the code generator


class command(Enum):  # Command enum type for the code generator

    Add = "+"  # Add command name in the code generator
    Sub = "-"  # Sub command name in the code generator
    Neg = "~"  # Neg command name in the code generator
    And = "&"  # And command name in the code generator
    Or = "|"   # Or command name in the code generator
    Not = "!"  # Not command name in the code generator
    Eq = "="   # Eq command name in the code generator
    Lt = "<"   # Lt command name in the code generator
    Gt = ">"   # Gt command name in the code generator
    Le = "<="  # Le command name in the code generator
    Ge = ">="  # Ge command name in the code generator
