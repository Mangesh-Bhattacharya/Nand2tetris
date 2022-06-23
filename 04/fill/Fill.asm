// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Mangesh Bhattacharya | 039-251-145

@beginning
        M=-1               //Black screen
        D=0         
        @SETSCREEN
        0;JMP

(LOOP)
        @KBD	        // Ready Keyboard
        D=M             // D resister becomes equal to 
        @SETSCREEN	
        D;JEQ           // If KBD=0 then set screen to 0 or white
        D=-1            // If key is pressed then set screen to all black

(SETSCREEN)             //Setting the screen D=new before jump here
        @ARG
        M=D             //No. of Bytes
        @beginning     
        D=D-M           
        @LOOP
        D;JEQ            
        
        @ARG
        D=M
        @beginning
        M=D             // beginning = ARG
        
        @SCREEN
        D=A              //D=Screen Address
        @8192           //(512 * 32) / 16
        D=D+A           // D=Byte passing last screen address
        @i
        M=D             //Write from Memory
        
(SETLOOP)    
        @i
        D=M-1
        M=D             //Write from Memory - i=i-1
        @LOOP
        D;JLT           //go back to Loop
        
        @beginning
        D=M             //Read from Memory - D=beginning           
        @i                
        A=M              // A register
        M=D             //M[current screen address] = status
        @SETLOOP
        0;JMP           //Infinite Loop