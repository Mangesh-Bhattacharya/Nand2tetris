// VMCommand:push constant 111
@111
D=A
// Push value into stack
@SP
A=M
M=D
@SP
M=M+1

// VMCommand:push constant 333
@333
D=A
// Push value into stack
@SP
A=M
M=D
@SP
M=M+1

// VMCommand:push constant 888
@888
D=A
// Push value into stack
@SP
A=M
M=D
@SP
M=M+1

// VMCommand:pop static 8
// Get the top element of stack
@SP
M=M-1
A=M
D=M
@StaticTest.8
M=D

// VMCommand:pop static 3
// Get the top element of stack
@SP
M=M-1
A=M
D=M
@StaticTest.3
M=D

// VMCommand:pop static 1
// Get the top element of stack
@SP
M=M-1
A=M
D=M
@StaticTest.1
M=D

// VMCommand:push static 3
@StaticTest.3
D=M
// Push value into stack
@SP
A=M
M=D
@SP
M=M+1

// VMCommand:push static 1
@StaticTest.1
D=M
// Push value into stack
@SP
A=M
M=D
@SP
M=M+1

// VMCommand:sub
// Get the top element of stack
@SP
M=M-1
A=M
D=M
// Store result temporarily
@R14
M=D
// Get the top element of stack
@SP
M=M-1
A=M
D=M
// Store result temporarily
@R13
M=D
@R13
D=M
@R14
D=D-M
// Push value into stack
@SP
A=M
M=D
@SP
M=M+1

// vm command:push static 8
@StaticTest.8
D=M
// push the value into stack
@SP
A=M
M=D
@SP
M=M+1

// vm command:add
// get the top element of stack
@SP
M=M-1
A=M
D=M
// store the result temporarily
@R14
M=D
// get the top element of stack
@SP
M=M-1
A=M
D=M
// store the result temporarily
@R13
M=D
@R13
D=M
@R14
D=D+M
// push the value into stack
@SP
A=M
M=D
@SP
M=M+1

