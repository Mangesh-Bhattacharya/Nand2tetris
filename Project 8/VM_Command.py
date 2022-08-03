"""
Dictionary for all Command_Types known as VMCommand.py file. Refering to the slides. (Updated)
"""


c_arithmetic = 1  # Arithmetic command
c_label = 2  # Label command
c_goto = 3  # Goto command
c_return = 4  # Return command
c_push = 5  # Push command
c_pop = 6  # Pop command
c_function = 7  # Function command
c_call = 8  # Call command
c_if = 9  # If command

"""
VM code commands as string for the top commands & the below Mem Options (Updated from slides)
"""
add = "push/pop"  # Add command
sub = "pop/pop"   # Sub command
negate = "push/pop"  # Neg command
eq = "push/pop"  # Eq command
gt = "push/pop"  # Gt command
lt = "push/pop"  # Lt command
And = "push/pop"  # And command
Or = "push/pop"  # Or command
Not = "push/pop"  # Not command
push = "push/pop"  # Push command
pop = "push/pop"  # Pop command
Label = "Label"  # Label command
IF = "goto-if"  # If command
ret = "return"  # Return command
goto = "goto"  # Goto command
function = "function"  # Function command
call = "call"  # Call command
# Arithmetic command
arithmetic = ("add, sub, lt, and , neg, eq, not, gt, or ")

"""
VM code Commands and its Memory Options.
"""
argument = 1  # Argument command
static = 2  # Static command
this = 3    # This command
that = 4   # That command
pointer = 5  # Pointer command
temp = 6  # Temp command
local = 7  # Local command
constant = 8  # Constant command

"""
Hack RAM in acronyms
"""
argument = "ARG"  # Argument command
static = "STATIC"  # Static command
this = "THIS"   # This command
that = "THAT"  # That command
pointer = "POINTER"  # Pointer command
temp = "TEMP"  # Temp command
local = "LCL"  # Local command
constant = "CONST"  # Constant command
