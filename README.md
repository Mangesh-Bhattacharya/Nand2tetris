# Nand2Tetris
There are two parts to the Nand2Tetris projects
- Part 1 consists of hardware projects from 1-6 
- Part 2 consists of Operating System projects from 7-12.

# Jack compiler
VM code is generated from source code in the Jack programming language. The translation is a two-stage process that begins with the compiler:
- The first stage involves converting jack high-level programs (.jack) to virtual machine code (.vm)
- The second step is translating virtual machine programs into hack assembly language (.asm).

In VM code, stacks are used to construct programs
```
.jack   == compilation ==>   .vm   == translation ==>   .asm 
```
Lastly, the hack platform is translated into binary code with the help of an assembler.
```
.asm   == assembly ==>   .hack
```

# Book or Text
The Elements of Computing Systems: Building a Modern Computer from First Principles

# Website
From https://www.nand2tetris.org/

