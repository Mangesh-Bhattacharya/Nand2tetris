# This is a subclass of Exception class and it is used to raise an error when the syntax is wrong.
class syntax_error_except(Exception):

    # Constructor of the class syntax_error_except that takes the line number and the expected statement as parameters and stores them in the class variables.
    # The constructor also calls the function print_error() to print the error message.
    def __init__(Self, Line, Expected, Message='syntax error {}. Your expected statement is \'{}\'.'):
        Self.Line = Line  # the line number of the error in the source code file
        Self.Message = Message
        # the expected statement that the user is trying to parse when the exception is raised by the interpreter
        Self.Expected = Expected
        # call the parent class constructor with the message as an argument to set the message of the exception class to the message of
        # the exception class with the line number and the expected statement as the arguments to be printed out by the interpreter when the exception is raised by
        # the interpreter when the exception is raised by the interpreter
        super().__init__(Self.Message.format(Self.Line, Self.Expected))
        return  # Return the error message in the correct format.

    # Override the string method to print the error message in the correct format.
    def __string__(Self):
        # return the message of the exception class as a string to be printed out by the interpreter when the exception is raised by the interpreter
        return Self.Message.format(Self.Line, Self.Expected)
