// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.
//RAM[2] = RAM[0]+RAM[1]

// Mangesh Bhattacharya
// Pseudo Code
// y=R1
// x=R0
// R2=0
// while(x > 0)
// {
//      R2 += y
//      x--    
// }
            @R0
            D=M
            @x
            M=D         // x = R0

            @R1
            D=M
            @y
            M=D         // y = R1

            @0
            D=A
            @R2
            M=D         // R2 = 0
    
    (WHILE)
            // LOOP condition Starts
            @x
            D=M
            @END
            D;JLE       //If x <= 0 then END
            // LOOP condition Ends

            // WHILE Start
            @y
            D=M
            @R2         // D = y
            M=D+M       // sum = sum + y (example mentioned in slides)
            @1
            D=A         // D = 1
            @x
            M=D-M       // x = x - 1
            // WHILE Ends

            @WHILE
            0;JMP       //Jump to LOOP start

    (END)
            @END
            0;JMP       //Code end for Infinite Loop
