//push constant 17

            @17
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//push constant 17

            @17
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//eq

            @SP
            AM=M-1
            D=M
            @SP
            AM=M-1
            D=M-D
            @SET_TRUE0
            D;JEQ
            @SP
            A=M
            M=0
            @SP_PLUS_ONE0
            0;JMP
            (SET_TRUE0)
            @SP
            A=M
            M=-1
            (SP_PLUS_ONE0)
            @SP
            M=M+1
//push constant 17

            @17
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//push constant 16

            @16
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//eq

            @SP
            AM=M-1
            D=M
            @SP
            AM=M-1
            D=M-D
            @SET_TRUE1
            D;JEQ
            @SP
            A=M
            M=0
            @SP_PLUS_ONE1
            0;JMP
            (SET_TRUE1)
            @SP
            A=M
            M=-1
            (SP_PLUS_ONE1)
            @SP
            M=M+1
//push constant 16

            @16
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//push constant 17

            @17
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//eq

            @SP
            AM=M-1
            D=M
            @SP
            AM=M-1
            D=M-D
            @SET_TRUE2
            D;JEQ
            @SP
            A=M
            M=0
            @SP_PLUS_ONE2
            0;JMP
            (SET_TRUE2)
            @SP
            A=M
            M=-1
            (SP_PLUS_ONE2)
            @SP
            M=M+1
//push constant 892

            @892
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//push constant 891

            @891
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//lt

            @SP
            AM=M-1
            D=M
            @SP
            AM=M-1
            D=M-D
            @SET_TRUE3
            D;JLT
            @SP
            A=M
            M=0
            @SP_PLUS_ONE3
            0;JMP
            (SET_TRUE3)
            @SP
            A=M
            M=-1
            (SP_PLUS_ONE3)
            @SP
            M=M+1
//push constant 891

            @891
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//push constant 892

            @892
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//lt

            @SP
            AM=M-1
            D=M
            @SP
            AM=M-1
            D=M-D
            @SET_TRUE4
            D;JLT
            @SP
            A=M
            M=0
            @SP_PLUS_ONE4
            0;JMP
            (SET_TRUE4)
            @SP
            A=M
            M=-1
            (SP_PLUS_ONE4)
            @SP
            M=M+1
//push constant 891

            @891
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//push constant 891

            @891
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//lt

            @SP
            AM=M-1
            D=M
            @SP
            AM=M-1
            D=M-D
            @SET_TRUE5
            D;JLT
            @SP
            A=M
            M=0
            @SP_PLUS_ONE5
            0;JMP
            (SET_TRUE5)
            @SP
            A=M
            M=-1
            (SP_PLUS_ONE5)
            @SP
            M=M+1
//push constant 32767

            @32767
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//push constant 32766

            @32766
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//gt

            @SP
            AM=M-1
            D=M
            @SP
            AM=M-1
            D=M-D
            @SET_TRUE6
            D;JGT
            @SP
            A=M
            M=0
            @SP_PLUS_ONE6
            0;JMP
            (SET_TRUE6)
            @SP
            A=M
            M=-1
            (SP_PLUS_ONE6)
            @SP
            M=M+1
//push constant 32766

            @32766
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//push constant 32767

            @32767
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//gt

            @SP
            AM=M-1
            D=M
            @SP
            AM=M-1
            D=M-D
            @SET_TRUE7
            D;JGT
            @SP
            A=M
            M=0
            @SP_PLUS_ONE7
            0;JMP
            (SET_TRUE7)
            @SP
            A=M
            M=-1
            (SP_PLUS_ONE7)
            @SP
            M=M+1
//push constant 32766

            @32766
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//push constant 32766

            @32766
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//gt

            @SP
            AM=M-1
            D=M
            @SP
            AM=M-1
            D=M-D
            @SET_TRUE8
            D;JGT
            @SP
            A=M
            M=0
            @SP_PLUS_ONE8
            0;JMP
            (SET_TRUE8)
            @SP
            A=M
            M=-1
            (SP_PLUS_ONE8)
            @SP
            M=M+1
//push constant 57

            @57
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//push constant 31

            @31
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//push constant 53

            @53
            D=A
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
//push constant 112

            @112
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
//neg

            @SP
            AM=M-1
            M=-M
            @SP
            M=M+1
//and

            @SP
            AM=M-1
            D=M
            @SP
            AM=M-1
            M=D&M
            @SP
            M=M+1
//push constant 82

            @82
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
//or

            @SP
            AM=M-1
            D=M
            @SP
            AM=M-1
            M=D|M
            @SP
            M=M+1
//not

            @SP
            AM=M-1
            M=!M
            @SP
            M=M+1
