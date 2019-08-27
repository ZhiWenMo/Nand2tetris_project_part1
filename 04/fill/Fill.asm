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

// Put your code here.

//start infinite loop
(LOOP)
    @KBD
    D=M
    @WHITE
    D;JEQ // if KBD=0 goto WHITE 

    @BLACK
    0;JMP // else goto BLACK

(BLACK)
   @i
   M=0
   
(BLACKLOOP)
    @KBD
    D=M
    @WHITE
    D;JEQ // if KBD=0 goto WHITE 

    @i
    D=M
    @8192
    D=D-A
    @LOOP
    D;JGE // if all the digits are black goto infinite loop

    @i
    D=M
    @SCREEN
    A=A+D
    M=-1 // black the digits

    @i
    M=M+1 // i++

    @BLACKLOOP
    0;JMP

(WHITE)
    @i
    M=0

(WHITELOOP)
    @KBD
    D=M
    @BLACK
    D;JNE // if KBD!=0 goto BLACK

    @i
    D=M
    @8192
    D=D-A
    @LOOP
    D;JGE // if all the digits are white goto infinite loop

    @i
    D=M
    @SCREEN
    A=A+D
    M=0 // white the digits

    @i
    M=M+1 // i++

    @WHITELOOP
    0;JMP
