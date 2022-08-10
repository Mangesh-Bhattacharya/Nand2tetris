////////////////////////////////////////////////////////////////////////////////////////////////

//  Name: Mangesh Bhattacharya 
//  Course: Computer Fundamentals
//  Code: DCN 250
//  Inst: Dr. Yousef Ashibani

////////////////////////////////////////////////////////////////////////////////////////////////

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


        @R0
        D=M             
        @a                       // Prevents R0 to not change after the program
        M=D                     // a = R0

        @R1
        D=M     
        @b                    // Prevents R1 to not change after the program
        M=D                  // b = R1

        @0
        D=A
        @R2
        M=D               // R2 = 0, sum resets

(LOOP)       // Loop condition starts
        @a
        D=M             // For Loop condition R0 loads     
        @END
        D;JLE         // if a <= 0 then go to END
            // Loop condition ends
        
           // Body of "While" starts
        @b                
        D=M         // D = b
        @R2
        M=D+M      // sum = sum + b

        @1
        D=A       // D = 1
        @a
        M=M-D    // a = a - 1          
          // Body of "While" ends

        @LOOP
        0;JMP   //Loop start jump
(END)
        @END
        0;JMP   //Infinite Loop
