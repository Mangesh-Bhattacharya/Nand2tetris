################################################################################################
"""
    Name: Mangesh Bhattacharya 
    Course: Computer Fundamentals
    Code: DCN 250
    Inst: Dr. Yousef Ashibani
"""
################################################################################################

# Variable Types from Variables.var_type.py file (for type checking)

from Variables.var_type import var_type


class vm_writer:  # Class for writing to VM file (.vm)

    # Constructor for vm_writer class (Output_File_Name is the name of the output file)
    def __init__(Self, Output_File_Name):
        # Open output file for writing (.vm)
        Self.open_prg_File(Output_File_Name)

    def WPush(Self, Seg, Ind):  # Write Push command to output file (.vm)
        # Write Push command to output file (.vm)
        Self.out_prg_File.write(("PUSH {} {}\n").format(Seg.Val, Ind))

    def WPop(Self, Seg, Ind):  # Write Pop command to output file (.vm)
        # Write Pop command to output file (.vm)
        Self.out_prg_File.write(("POP {} {}\n").format(Seg.Val, Ind))

    def WArith(Self, Comm):  # Write Arithmetic command to output file (.vm)
        # Write command name to output file (.vm)
        Self.Out_prg_File.write(("{}\n").format(Comm.Name.Low()))

    def WLabel(Self, Label):  # Write Label command to output file (.vm)
        # Write label name to output file (.vm)
        Self.Out_prg_File.write(("Label {}\n").format(Label))

    def WGoto(Self, Label):  # Write Goto command to output file (.vm)
        # Write Goto command to output file (.vm)
        Self.Out_prg_File.write(("GOTO {}\n").format(Label))

    def WIf(Self, Label):  # Write If-Goto command to output file (.vm)
        # Write If-Goto command to output file (.vm)
        Self.Out_prg_File.write(("IF-GOTO {}\n").format(Label))

    def WCall(Self, Name, Num):  # Write Call command to output file (.vm)
        # Write Call command to output file (.vm)
        Self.Out_prg_File.write(("CALL {} {}\n").format(Name, Num))

    def WFunction(Self, Name, lcl):  # Write Function command to output file (.vm)
        # Write Function command to output file (.vm)
        Self.Out_prg_File.write(("FUNCTION {} {}\n").format(Name, lcl))

    def WReturn(Self):  # Write Return command to output file (.vm)
        # Write Return command to output file (.vm)
        Self.Out_prg_File.write("RETURN\n")

    def Close(Self):
        # Close output file (.vm)
        Self.out_prg_File.close()

    def open_prg_File(Self, File_Name):  # Open output file (.vm)
        # Open output file (.vm)
        Self.out_prg_File = open(File_Name, "a")
