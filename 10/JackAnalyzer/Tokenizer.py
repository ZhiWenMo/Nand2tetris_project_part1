# token type
import sys
import os
KEYWORD = "keyword"
SYMBOL = "symbol"
IDENTIFIER = "identifier"
INT_CONST = "int_const"
STRING_CONST = "string_const"


class JackTokenizer:
    def __init__(self, input_file_path):
        """Open input file & some specification
        input file: file path
        """
        self._keyword = ["class", "constructor", "function",
                         "method", "field", "static", "var", "int",
                         "char", "boolean", "void", "true", "false",
                         "null", "this", "let", "do", "if", "else", "while", "return"]

        self._symbol = ["{", "}", "(", ")", "[", "]",
                        ".", ",", ";", "+", "-", "*", "/", "&", "|", "<", ">", "=", "~"]

        self.input_file_steam = open(input_file_path, "r")

        self._current_line = self.input_file_steam.readline()
        self.token_gen = self._token_generator()
        self._current_token = None

    def _token_generator(self):
        comment_start = False
        while self._current_line:
            # skip single line comment and blank line
            if self._current_line.strip().startswith("//") or self._current_line.strip() == "":
                self._current_line = self.input_file_steam.readline()
                continue

            if self._current_line.strip().startswith(("/*", "/**")) and self._current_line.strip().endswith("*/"):
                self._current_line = self.input_file_steam.readline()
                continue

            # skip multile line comment
            if self._current_line.strip().startswith(("/*", "/**")) and not comment_start:
                comment_start = True
                self._current_line = self.input_file_steam.readline()
                continue

            if self._current_line.strip().endswith("*/") and comment_start:
                comment_start = False
                self._current_line = self.input_file_steam.readline()
                continue

            if comment_start:
                self._current_line = self.input_file_steam.readline()
                continue

            line = self._current_line.rsplit("//")[0].strip()

            temp_token = ""
            start_string = False

            for c in line:
                # handle start of the string
                if c == '"' and not start_string:
                    start_string = True
                    temp_token += c
                    continue

                # handle the end of the string
                if c == '"' and start_string:
                    temp_token += c
                    yield temp_token
                    temp_token = ""
                    start_string = False
                    continue
                # when encounter space yield temp token if not empty and clean it
                if c == " " and not start_string:
                    if temp_token != "":
                        yield temp_token
                        temp_token = ""
                    continue

                # when encounter symbol yield temp token if not empty and clean it
                # then yield the symbol
                if c in self._symbol and not start_string:
                    if temp_token != "":
                        yield temp_token
                        temp_token = ""
                    yield c
                    continue

                temp_token += c

            self._current_line = self.input_file_steam.readline()

    def hasMoreTokens(self):
        """Do we have more token in the input?
        """
        return self.advance()

    def advance(self):
        """Get the next token
        """
        try:
            self._current_token = next(self.token_gen)
            return True
        except StopIteration:
            return False

    def tokenType(self):
        """Returns the type of the current token.
        """
        if self._current_token in self._keyword:
            return KEYWORD

        if self._current_token in self._symbol:
            return SYMBOL

        if self._current_token.isdigit():
            return INT_CONST

        if self._current_token.startswith('"') and self._current_token.endswith('"'):
            return STRING_CONST

        return IDENTIFIER

    def keyWord(self):
        """Returns the keyword which is the current token.
        """
        if self.tokenType() is KEYWORD:
            token = self._current_token
            return token

    def symbol(self):
        """Returns the character which is the current token.
        """
        if self.tokenType() is SYMBOL:
            token = self._current_token
            return token

    def identifier(self):
        """Returns the identifier which is the current token.
        """
        if self.tokenType() is IDENTIFIER:
            token = self._current_token
            return token

    def intVal(self):
        """Returns the integer value which is the current token.
        """
        if self.tokenType() is INT_CONST:
            token = self._current_token
            return token

    def stringVal(self):
        """Returns the string value of the current token,
        without the double quotes.
        """
        if self.tokenType() is STRING_CONST:
            token = self._current_token.strip('"')
            return token


XML_MARK_UP = {"<": "&lt;", ">": "&gt;", '"': "&quot;", "&": "&amp;"}


def mark_up_symbol(sym):
    return XML_MARK_UP[sym] if sym in XML_MARK_UP else sym


def tokenizer_test(inputFileDir, outPutFileDir):
    jackfilenames = [f for f in os.listdir(
        inputFileDir) if f.endswith(".jack")]

    for jackfilename in jackfilenames:
        inputfilepath = os.path.join(inputFileDir, jackfilename)
        outputfilepath = os.path.join(
            outPutFileDir, jackfilename.split(".")[0]+"T.xml")

        jt = JackTokenizer(inputfilepath)

        writer = open(outputfilepath, "w")

        writer.write("<tokens>\n")
        while jt.hasMoreTokens():
            if jt.tokenType() is KEYWORD:
                writer.write("<keyword> " + jt.keyWord() + " </keyword>\n")

            if jt.tokenType() is SYMBOL:
                write_symbol = mark_up_symbol(jt.symbol())

                writer.write("<symbol> " + write_symbol + " </symbol>\n")

            if jt.tokenType() is INT_CONST:
                writer.write("<integerConstant> " +
                             jt.intVal() + " </integerConstant>\n")

            if jt.tokenType() is STRING_CONST:
                writer.write("<stringConstant> " +
                             jt.stringVal() + " </stringConstant>\n")

            if jt.tokenType() is IDENTIFIER:
                writer.write("<identifier> " +
                             jt.identifier() + " </identifier>\n")

        writer.write("</tokens>\n")

        writer.close()

        print("Write: " + outputfilepath)

    print("All files wrote!")


def main():
    inputfiledir = sys.argv[1]
    outputfiledir = sys.argv[2]
    tokenizer_test(inputfiledir, outputfiledir)


if __name__ == "__main__":
    main()
