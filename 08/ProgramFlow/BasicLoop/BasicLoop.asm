//push constant 0    

            @0
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//pop local 0         

            @0
            D=A
            @LCL
            D=D+M
            @i
            M=D
            @SP
            AM=M-1
            D=M
            @i
            A=M
            M=D
//label LOOP_START

            (LOOP_START)
//push argument 0    

            @0
            D=A
            @ARG
            A=D+M
            D=M
            @SP
            A=M
            M=D
            @SP
            M=M+1
//push local 0

            @0
            D=A
            @LCL
            A=D+M
            D=M
            @SP
            A=M
            M=D
            @SP
            M=M+1
//add

            @SP
            AM=M-1
            D=M
            @SP
            AM=M-1
            M=D+M
            @SP
            M=M+1
//pop local 0	        

            @0
            D=A
            @LCL
            D=D+M
            @i
            M=D
            @SP
            AM=M-1
            D=M
            @i
            A=M
            M=D
//push argument 0

            @0
            D=A
            @ARG
            A=D+M
            D=M
            @SP
            A=M
            M=D
            @SP
            M=M+1
//push constant 1

            @1
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//sub

            @SP
            AM=M-1
            D=M
            @SP
            AM=M-1
            M=M-D
            @SP
            M=M+1
//pop argument 0      

            @0
            D=A
            @ARG
            D=D+M
            @i
            M=D
            @SP
            AM=M-1
            D=M
            @i
            A=M
            M=D
//push argument 0

            @0
            D=A
            @ARG
            A=D+M
            D=M
            @SP
            A=M
            M=D
            @SP
            M=M+1
//if-goto LOOP_START  

            @SP
            AM=M-1
            D = M
            @LOOP_START
            D;JNE
//push local 0

            @0
            D=A
            @LCL
            A=D+M
            D=M
            @SP
            A=M
            M=D
            @SP
            M=M+1
