class Parser:
    def __init__(self, input_file):
        self.file = open(input_file, "r")
        self.current_command = None

    def hasMoreCommands(self):
        """[Does the asm has more commands?]

        Returns:
            [boolean] -- [no description] 
        """
        try:
            line = next(self.file).strip()
            self.current_command = line.split("//")[0].strip()
            # handle inline comment
        except StopIteration:
            return False
        return True

    def advance(self):
        """[Read the next command if exists.]
        """
        self.hasMoreCommands()

    @property
    def commandType(self):
        """[Return the type of current command:]
        @Xxx is A_COMMAND, Xxx is either a symbol or a number
        dest = comp;jump is C_COMMAND
        (Xxx) is L_COMMAND, where Xxx is a symbol

        Returns:
            [command type] -- [the type of current command.]
        """
        command_type = "C_COMMAND"
        if self.current_command.startswith("//") or self.current_command == "":
            command_type = None
            # ignore space and comment line

        if self.current_command.startswith("@"):
            command_type = "A_COMMAND"

        if self.current_command.startswith("("):
            command_type = "L_COMMAND"
        return command_type

    @property
    def symbol(self):
        """[Returns the symbol or decimal Xxx of the current command]
        Should be called only when commandType is A_COMMAND  or L_COMMAND.

        Raises:
            ValueError: [when commandType is nor A_COMMAND or L_COMMAND]

        Returns:
            [symbol] -- [symbol or decimal]
        """
        if self.commandType == "A_COMMAND":
            return self.current_command[1:]
        elif self.commandType == "L_COMMAND":
            return self.current_command[1:-1]
        else:
            raise ValueError(self.current_command, "commandType: ",
                             self.commandType, "not A_COMMAND or L_COMMAND")

    @property
    def dest(self):
        """[Returns the dest mnemonic in the current C-command.]

        Raises:
            ValueError: [no dest]

        Returns:
            [dest strings] -- [8 possibilities]
        """
        self.sp_elem = self.current_command.split("=")
        if len(self.sp_elem) == 2:
            self.lhs, self.rhs = self.sp_elem
            return self.lhs.strip()
        else:
            return None

    @property
    def comp(self):
        """[Returns the comp mnemonic in the current C-commnad.]

        Returns:
            [comp strings] -- [28 possibilities]
        """
        if self.dest is None:
            self.c_sp_elem = self.sp_elem[0].split(";")
        else:
            self.c_sp_elem = self.rhs.split(";")

        if len(self.c_sp_elem) == 2:
            self.c_lhs, self.c_rhs = self.c_sp_elem

            return self.c_lhs.strip()
            # if has jump mnemonic return left hand side of the colon.
        else:
            self.c_rhs = None
            return self.c_sp_elem[0].strip()
            # else return the only comp mnemonic

    @property
    def jump(self):
        """[Returns the jump mnemonic in the current C-commnad.]

        Returns:
            [jump string] -- [8 possibilities]
        """
        _ = self.comp
        return self.c_rhs


class Code:
    def __init__(self):
        self.dest_table = {
            "M": "001",
            "D": "010",
            "MD": "011",
            "A": "100",
            "AM": "101",
            "AD": "110",
            "AMD": "111"
        }

        self.jump_table = {
            "JGT": "001",
            "JEQ": "010",
            "JGE": "011",
            "JLT": "100",
            "JNE": "101",
            "JLE": "110",
            "JMP": "111"
        }

        self.a_1 = set(["M", "!M", "-M", "M+1", "M-1",
                        "D+M", "D-M", "M-D", "D&M", "D|M"])

        self.comp_table = {
            "0": "101010",
            "1": "111111",
            "-1": "111010",
            "D": "001100",
            "A": "110000",
            "!D": "001101",
            "!A": "110001",
            "-D": "001111",
            "-A": "110011",
            "D+1": "011111",
            "A+1": "110111",
            "D-1": "001110",
            "A-1": "110010",
            "D+A": "000010",
            "D-A": "010011",
            "A-D": "000111",
            "D&A": "000000",
            "D|A": "010101"
        }

    def dest(self, mnemonic):
        return "000" if mnemonic is None else self.dest_table[mnemonic]

    def comp(self, mnemonic):
        if mnemonic in self.a_1:
            a = "1"
            rp_mn = mnemonic.replace("M", "A")
        else:
            a = "0"
            rp_mn = mnemonic

        return a + self.comp_table[rp_mn]

    def jump(self, mnemonic):
        return "000" if mnemonic is None else self.jump_table[mnemonic]


class SymbolTable:
    def __init__(self):
        self.table = {
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,
            "SCREEN": 16384,
            "KBD": 24576
        }

        for i in range(16):
            self.table["R{}".format(i)] = i

    def addEntry(self, symbol, address):
        self.table[symbol] = address

    def contains(self, symbol):
        return symbol in self.table

    def GetAddress(self, symbol):
        return self.table[symbol]


def int215bits(integer):
    integer = int(integer)
    return '{0:015b}'.format(integer)


if __name__ == "__main__":
    import os
    import sys

    path = sys.argv[1]
    fileprefix = os.path.dirname(path)
    infilename = os.path.basename(path)
    outfilename = infilename.split(".")[0]+".hack"
    parser = Parser(path)
    code = Code()
    symboltable = SymbolTable()

    a_left_bits = "0"
    c_left_bits = "111"

    rom_address = -1
    ram_address = 16

    # first pass
    labels = []
    while True:
        if parser.hasMoreCommands() is False:
            break
        if parser.commandType is None:
            continue
        if parser.commandType == "L_COMMAND":
            labels.append(parser.symbol)
            continue
        if parser.commandType in ["A_COMMAND", "C_COMMAND"]:
            rom_address += 1
            if labels is not None:
                for label in labels:
                    symboltable.addEntry(label, rom_address)
                labels = []

    outputfile_path = os.path.join(fileprefix, outfilename)
    writer = open(outputfile_path, "w")

    # second pass
    parser = Parser(path)
    while True:
        if parser.hasMoreCommands() is False:
            break
        if parser.commandType is None:
            continue

        if parser.commandType == "A_COMMAND":
            tmp_symbol = parser.symbol
            if not tmp_symbol.isdigit():
                if symboltable.contains(tmp_symbol):
                    tmp_symbol = symboltable.GetAddress(tmp_symbol)
                else:
                    symboltable.addEntry(tmp_symbol, ram_address)
                    tmp_symbol = ram_address
                    ram_address += 1
            bin_code = a_left_bits + int215bits(tmp_symbol) + "\n"
            writer.write(bin_code)

        if parser.commandType == "C_COMMAND":
            dest = code.dest(parser.dest)
            comp = code.comp(parser.comp)
            jump = code.jump(parser.jump)

            bin_code = c_left_bits + comp + dest + jump + "\n"
            writer.write(bin_code)

    writer.close()

    print("Assemble finished!")
