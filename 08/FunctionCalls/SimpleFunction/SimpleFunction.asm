//function SimpleFunction.test 2

            (SimpleFunction.vm.SimpleFunction.test)

            @0
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1

            @0
            D=A
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
//push local 1

            @1
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
//not

            @SP
            AM=M-1
            M=!M
            @SP
            M=M+1
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
//add

            @SP
            AM=M-1
            D=M
            @SP
            AM=M-1
            M=D+M
            @SP
            M=M+1
//push argument 1

            @1
            D=A
            @ARG
            A=D+M
            D=M
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
//return

            @LCL
            D=M
            @R13
            M=D
            @5
            D=D-A
            A=D
            D=M
            @R14
            M=D
            @SP
            AM=M-1
            D=M
            @ARG
            A=M
            M=D
            @ARG
            D=M
            @SP
            M=D+1
            @R13
            MD=M-1
            A=D
            D=M
            @THAT
            M=D
            @R13
            MD=M-1
            A=D
            D=M
            @THIS
            M=D
            @R13
            MD=M-1
            A=D
            D=M
            @ARG
            M=D
            @R13
            MD=M-1
            A=D
            D=M
            @LCL
            M=D
            @R14
            D=M
            A=D
            0;JMP
